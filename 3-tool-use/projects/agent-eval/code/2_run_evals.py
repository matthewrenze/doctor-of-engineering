# Import packages
import time
from common.log import Log
from common.console import warn
from common.parameters import Parameters
from environments.env_factory import EnvFactory
from evals.eval_factory import EvalFactory
from models.cost_calculator import CostCalculator
from models.model_factory import ModelFactory
from agents.agent_factory import AgentFactory
from results.results_manager import ResultsManager
from summaries.summary_manager import SummaryManager
from agents.dialogue_writer import DialogueWriter

# Set agents
agent_names = [
    # "baseline",
    "react-v3",
]

# Set models
model_names = [
    # "claude-sonnet-4-0",
    # "claude-opus-4-1",
    # "deepseek-r1",
    # "deepseek-v3",
    # "gemini-2.5-flash",
    # "gemini-2.5-flash-lite",
    # "gemini-2.5-pro",
    # "gpt-4.1",
    "gpt-4.1-mini",
    # "gpt-5",
    # "gpt-5-mini",
    # "grok-3",
    # "grok-3-mini"
]

# Set evals
# Note: (eval_name, env_name, max_steps)
eval_size = 10
eval_env_names = [
    # ("debug-all-tools", "open-qa", 10),
    # ("debug-finish", "open-qa", 10),
    # ("debug-calculate", "open-qa", 10),
    # ("debug-list-files", "open-qa", 10),
    # ("debug-read-file", "open-qa", 10),
    # ("debug-search-web", "open-qa", 10),
    # ("debug-read-html", "open-qa", 10),
    # ("debug-download-file", "open-qa", 10),
    # ("debug-execute-code", "open-qa", 10),
    # ("gaia", "open-qa", 20),
    # ("gpqa-diamond", "mcqa", 20),
    # ("hle", "open-qa", 20),
    # ("mmlu-pro", "mcqa", 20),
    # ("simple-qa", "open-qa", 20),
    # ("tw-simple", "textworld", 20),
    # ("tw-coin", "textworld", 20),
    # ("tw-treasure", "textworld", 100),
    # ("tw-cooking", "textworld", 50),
]

# Set parameters
# max_steps = 20
sleep_time = 1

# Create the runs
runs = []
for agent_name in agent_names:
    for model_name in model_names:
        for eval_env_name in eval_env_names:
            eval_name, env_name, max_steps = eval_env_name
            eval_name = f"{eval_name}-{eval_size}"
            params = Parameters(
                agent_name = agent_name,
                model_name = model_name,
                env_name = env_name,
                eval_name = eval_name,
                max_steps = max_steps
            )
            runs.append(params)

# Create components
model_factory = ModelFactory()
agent_factory = AgentFactory()
eval_factory = EvalFactory()
env_factory = EnvFactory()
cost_calculator = CostCalculator()
agent_writer = DialogueWriter()

for params in runs:
    print(f"--- Running {params.agent_name} - {params.model_name} - {params.eval_name} ---")

    # Create components
    results_manager = ResultsManager()
    summary_manager = SummaryManager()

    # Create entities
    model = model_factory.create(params)
    agent = agent_factory.create(params, model)
    eval = eval_factory.create(params)
    env = env_factory.create(params, eval)
    num_episodes = len(eval)

    # Set up summaries
    if summary_manager.exists(params):
        warn(f"Summary for {params.agent_name} - {params.model_name} - {params.eval_name} already exists.")
        input("Press Enter to continue...")

    for episode_id in range(num_episodes):
        log = Log(params, episode_id)
        log.head(f"--- Starting {params.agent_name} - {params.model_name} - {params.eval_name} - episode {episode_id + 1} / {num_episodes} ---")
        episode = eval.iloc[episode_id].to_dict()
        answer = ""
        reward = 0.0
        step_id = 0

        try:

            # Reset the environment
            task, state = env.reset(episode_id)
            log.info(f"Task: {task}")
            log.info(f"State: {state}\n")

            # Reset the agent
            agent.reset(task)
            step_id = 0

            # Create result row
            result_row = results_manager.create(params)
            result_row.episode_id = episode_id
            result_row.episode = task
            result_row.start_time = time.time()
            if "question" in episode:
                result_row.type = episode["topic"]
                result_row.question = episode["question"]
                result_row.correct_answer = episode["answer"]

            # Run the agent in the environment
            for step_id in range(params.max_steps):
                log.info(f"# Step {step_id + 1}")

                # Get the agent's action
                thought, action = agent.act(state)
                log.info(f"Thought: {thought}")
                log.info(f"Action: {action}")

                # Get the environment's state
                state, reward, is_done = env.step(action)
                state_text = state if isinstance(state, str) else f"[{len(state)} bytes]"
                log.info(f"State: {state_text}")

                # Handle end of episode
                if is_done:
                    if params.env_name in ["mcqa", "open-qa"]:
                        answer = action.split('(')[1].rstrip(')')
                    break

                # Sleep for n seconds to avoid API throttling
                time.sleep(sleep_time)
                log.info("")

        except Exception as e:
            result_row.error = str(e)
            log.error(e)

        # Update result row
        result_row.stop_time = time.time()
        result_row.total_time = result_row.stop_time - result_row.start_time
        result_row.agent_answer = answer
        result_row.reward = reward
        result_row.steps = step_id + 1
        result_row.input_tokens = model.input_tokens
        result_row.output_tokens = model.output_tokens
        result_row.total_tokens = model.total_tokens
        result_row.input_cost = cost_calculator.get_input_cost(params.model_name, model.input_tokens)
        result_row.output_cost = cost_calculator.get_output_cost(params.model_name, model.output_tokens)
        result_row.total_cost = result_row.input_cost + result_row.output_cost
        result_row.reward_per_step = reward / (step_id + 1)
        result_row.reward_per_token = (reward / model.total_tokens) if model.total_tokens > 0 else 0.0
        results_manager.add(result_row)

        # Log the agent messages
        agent_writer.write(params, episode_id, agent.messages)

        # Log the results
        log.info(f"Reward: {reward}")
        log.head("--- End of task ---\n")
        log.close()

        # Sleep for n seconds to avoid API throttling
        time.sleep(sleep_time)

    # Save the results
    results_manager.save()

    # Save the summary
    results = results_manager.get_table()
    summary = summary_manager.summarize(results)
    summary_manager.append(summary)

    # Display the summaries
    print(f"Total Tasks: {summary.tasks}")
    print(f"Correct Tasks: {summary.successes}")
    print(f"Accuracy: {summary.accuracy:.0%}")
    print(f"Total Tokens: {summary.total_tokens}")
    print(f"Total Cost: ${summary.total_cost:.2f}")
    print(f"Total Time: {summary.total_time:.2f} seconds")
    print(f"Avg Reward per Task: {summary.avg_reward_per_task:.2f}")
    print(f"Avg Reward per Step: {summary.avg_reward_per_step:.4f}")
    print(f"Avg Reward per Token: {summary.avg_reward_per_token:.6f}")
    print(" --- END OF EVAL ---" )
    print("")

