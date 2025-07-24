# Import packages
import time
from environments.env_factory import EnvFactory
from evals.eval_factory import EvalFactory
from models.model_factory import ModelFactory
from agents.agent_factory import AgentFactory
from results.results_manager import ResultsManager
from summaries.summary_manager import SummaryManager

# Set parameters
agent_name = "human"
model_name = "gpt-4.1"
eval_name = "alfworld-thor-level-1-1"
max_steps = 50

# Create components
model_factory = ModelFactory()
agent_factory = AgentFactory()
eval_factory = EvalFactory()
env_factory = EnvFactory()
results_manager = ResultsManager()
summary_manager = SummaryManager()

# Create entities
model = model_factory.create(model_name)
agent = agent_factory.create(agent_name, model)
eval = eval_factory.create(eval_name)
env = env_factory.create(eval_name, eval)
task_count = len(eval)

# Set up summaries
summary_manager.load()
if summary_manager.exists(agent_name, model_name, eval_name):
    print(f"WARNING: Summary for {agent_name} - {model_name} - {eval_name} already exists.")
    input("Press Enter to continue...")

for task_id in range(task_count):
    print(f"--- Task {task_id + 1} / {task_count} ---")
    task = eval[task_id]
    answer = ""
    reward = 0.0

    # Create result row
    result_row = results_manager.create()
    result_row.agent_name = agent_name
    result_row.model_name = model_name
    result_row.eval_name = eval_name
    result_row.task_id = task_id

# try:

    # Reset the agent and environment
    state = env.reset(task_id)
    agent.reset()
    step_id = 0

    # Run the agent in the environment
    for step_id in range(max_steps):
        print(f"# Step {step_id + 1}")
        # env.render()
        action = agent.act(state)
        state, reward, is_done = env.step(action)
        time.sleep(1)

        if is_done:
            print(f"Is Done: {is_done}")
            print(f"Final State: {state.get('text', '')}")
            print(f"Reward: {reward}")
            break

        print()

# except Exception as e:
#     print(f"ERROR: {e}")
#     result_row.error = str(e)

    # Update result row
    result_row.agent_answer = None
    result_row.reward = reward
    result_row.steps = step_id + 1
    result_row.input_tokens = model.input_tokens
    result_row.output_tokens = model.output_tokens
    result_row.total_tokens = model.total_tokens
    result_row.reward_per_step = reward / (step_id + 1)
    result_row.reward_per_token = (reward / model.total_tokens) if model.total_tokens > 0 else 0.0
    results_manager.add(result_row)
    print("--- END OF TASK ---\n")

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

