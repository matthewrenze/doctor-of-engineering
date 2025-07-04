import time
import pandas as pd
from results.result_row import DetailRow
from environments.env_factory import EnvFactory
from evals.eval_factory import EvalFactory
from models.model_factory import ModelFactory
from agents.agent_factory import AgentFactory

# Set parameters
task_count = 100
max_steps = 10

# Create factories
eval_factory = EvalFactory()
env_factory = EnvFactory()
model_factory = ModelFactory()
agent_factory = AgentFactory()

# Create entities
eval = eval_factory.create("hotpotqa", task_count)
env = env_factory.create(eval)
model = model_factory.create()
agent = agent_factory.create(model)

results = []

for task_id in range(task_count):
    print(f"--- Task {task_id + 1} / {task_count} ---")
    task = eval[task_id]
    answer = ""
    reward = 0.0

    # Create result row
    detail_row = DetailRow()
    detail_row.task_id = task_id
    detail_row.type = task["type"]
    detail_row.question = task["question"]
    detail_row.correct_answer = task["answer"]

    try:

        obs = env.reset()
        agent.reset()
        step_id = 0

        for step_id in range(max_steps):
            print(f"# Step {step_id + 1}")
            action = agent.act(obs)
            obs, reward, is_done = env.step(action)

            if is_done:
                answer = action.split('[')[1].rstrip(']')
                break

            print()

    except Exception as e:
        print(f"ERROR: {e}")
        detail_row.error = str(e)

    # Update result row
    detail_row.agent_answer = answer
    detail_row.reward = reward
    detail_row.steps = step_id + 1
    detail_row.input_tokens = model.input_tokens
    detail_row.output_tokens = model.output_tokens
    detail_row.total_tokens = model.total_tokens
    detail_row.reward_per_step = reward / (step_id + 1)
    detail_row.reward_per_token = (reward / model.total_tokens) if model.total_tokens > 0 else 0.0
    results.append(detail_row)
    print("--- END OF TASK ---\n")

    # # DEBUG: Wait for user input to continue to the next task
    # input("Press Enter to continue...")

    # Sleep for 1 second to avoid API throttling
    time.sleep(1)

# Save the results
results = pd.DataFrame([row.__dict__ for row in results])
results_file_path = f"../data/results/results-{task_count}.csv"
results.to_csv(results_file_path, index=False)

# Calculate the results
total_score = results['reward'].sum()
accuracy = total_score / task_count

# Display the results
print(f"Eval Size: {task_count}")
print(f"Total Tasks: {task_count}")
print(f"Correct Tasks: {results['reward'].sum()}")
print(f"Avg Reward: {total_score} / {task_count}")
print(f"Accuracy: {accuracy:.2%}")
print(f"Reward per Step: {results['reward_per_step'].mean():.4f}")
print(f"Reward per Token: {results['reward_per_token'].mean():.4f}")

