# Import packages
import time
from common.parameters import Parameters
from environments.env_factory import EnvFactory
from evals.eval_factory import EvalFactory
from graders.grader_factory import GraderFactory
from models.model_factory import ModelFactory
from agents.agent_factory import AgentFactory
from results.results_manager import ResultsManager
from summaries.summary_manager import SummaryManager

# Set parameters
params = Parameters(
    agent_name = "react",
    model_name = "gpt-4.1",
    eval_name = "gaia-test-10",
    max_steps = 10
)

# Create components
model_factory = ModelFactory()
agent_factory = AgentFactory()
eval_factory = EvalFactory()
grader_factory = GraderFactory()
env_factory = EnvFactory()
results_manager = ResultsManager()
summary_manager = SummaryManager()

# Create entities
model = model_factory.create(params)
agent = agent_factory.create(params, model)
eval = eval_factory.create(params)
grader = grader_factory.create()
env = env_factory.create(params, eval, grader)
num_episodes = len(eval)

# Set up summaries
summary_manager.load()
if summary_manager.exists(params):
    print(f"WARNING: Summary for {params.agent_name} - {params.model_name} - {params.eval_name} already exists.")
    input("Press Enter to continue...")

for episode_id in range(num_episodes):
    print(f"--- Task {episode_id + 1} / {num_episodes} ---")
    episode = eval.iloc[episode_id]
    answer = ""
    reward = 0.0
    step_id = 0

    # Create result row
    result_row = results_manager.create(params)
    result_row.episode_id = episode_id
    result_row.type = "General Assistance" # task["topic"]
    result_row.task = episode["task"]
    result_row.correct_answer = episode["answer"]

    try:

        # Reset the agent and environment
        obs = env.reset(episode_id)
        agent.reset()
        step_id = 0

        # Run the agent in the environment
        for step_id in range(params.max_steps):
            print(f"# Step {step_id + 1}")
            action = agent.act(obs)
            obs, reward, is_done = env.step(action)

            if is_done:
                answer = action.split('(')[1].rstrip(')')
                break

            print()

    except Exception as e:
        print(f"ERROR: {e}")
        result_row.error = str(e)

    # Update result row
    result_row.agent_answer = answer
    result_row.reward = reward
    result_row.steps = step_id + 1
    result_row.input_tokens = model.input_tokens
    result_row.output_tokens = model.output_tokens
    result_row.total_tokens = model.total_tokens
    result_row.reward_per_step = reward / (step_id + 1)
    result_row.reward_per_token = (reward / model.total_tokens) if model.total_tokens > 0 else 0.0
    results_manager.add(result_row)
    print("--- END OF TASK ---\n")

    # Sleep for 1 second to avoid API throttling
    time.sleep(1)

# Save the results
results_manager.save()

# Save the summary
results = results_manager.get_table()
summary = summary_manager.summarize(results)
summary_manager.add(summary)
summary_manager.save()

# Display the summaries
print(f"Total Tasks: {summary.tasks}")
print(f"Correct Tasks: {summary.successes}")
print(f"Accuracy: {summary.accuracy:.0%}")
print(f"Avg Reward per Task: {summary.avg_reward_per_task:.2f}")
print(f"Avg Reward per Step: {summary.avg_reward_per_step:.4f}")
print(f"Avg Reward per Token: {summary.avg_reward_per_token:.6f}")

