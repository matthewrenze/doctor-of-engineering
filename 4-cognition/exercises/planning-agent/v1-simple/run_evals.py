# Import packages
import time
from common.log import Log
from common.console import warn
from common.parameters import Parameters
from details.details_manager import DetailsManager
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
    "v1-simple"
]

# Set models
model_names = [
    "gpt-4.1-mini",
    # "gpt-5-mini",
]

# Set evals
# Note: (eval_name, env_name, max_steps)
eval_size = 100
eval_env_names = [
    ("tw-simple-1", "textworld", 20),
    ("tw-coin-1", "textworld", 100),
    ("tw-coin-2", "textworld", 100),
    ("tw-coin-3", "textworld", 100),
    ("tw-treasure-1", "textworld", 20),
    ("tw-treasure-2", "textworld", 40),
    ("tw-treasure-3", "textworld", 60),
    ("tw-cooking-1", "textworld", 20),
    ("tw-cooking-2", "textworld", 80),
    ("tw-cooking-3", "textworld", 100),
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
            params = Parameters(
                agent_name = agent_name,
                agent_version = int(agent_name.split("-")[0][1:]),
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
    num_episodes = min(len(eval), eval_size)

    # Set up summaries
    if summary_manager.exists(params):
        warn(f"Summary for {params.agent_name} - {params.model_name} - {params.eval_name} already exists.")
        input("Press Enter to continue...")

    for episode_id in range(num_episodes):

        # Create the log
        log = Log(params, episode_id)
        log.head(f"--- Starting {params.agent_name} - {params.model_name} - {params.eval_name} - episode {episode_id + 1} / {num_episodes} ---")

        # Create the details manager
        details_manager = DetailsManager(params, episode_id)

        # Create the episode
        episode = eval.iloc[episode_id].to_dict()
        answer = ""
        reward = 0.0
        step_id = 0

        try:

            # Reset the environment
            state = env.reset(episode_id)
            log.info(f"Task: {state.task}")
            log.info(f"State:")
            log.info(f"  Location: {state.location}")
            log.info(f"  Description: {state.description}")
            log.info(f"  Inventory: {state.inventory}")
            log.info(f"  Score: {state.score}")
            log.info("")

            # Reset the agent
            agent.reset(state.task)
            step_id = 0

            # Create result row
            result_row = results_manager.create(params)
            result_row.episode = episode_id + 1
            result_row.task = state.task
            result_row.start_time = time.time()

            # Create the details rows
            details_row = details_manager.create()
            details_row.step_id = step_id
            details_row.task = state.task
            details_row.location = state.location
            details_row.description = state.description
            details_row.inventory = state.inventory
            details_row.score = state.score
            details_manager.add(details_row)

            # Run the agent in the environment
            for step_id in range(params.max_steps):
                log.info(f"# Step {step_id + 1}")

                # Get the agent's action
                plan, thought, action = agent.act(state)
                log.info(f"Agent:")
                log.plan(f"  Plan:\n{plan}")
                log.info(f"  Thought: {thought}")
                log.info(f"  Action: {action}")

                # Get the environment's state
                state, reward, is_done = env.step(action)
                log.info(f"State:")
                log.info(f"  Feedback: {state.feedback}")
                log.info(f"  Location: {state.location}")
                log.info(f"  Description: {state.description}")
                log.info(f"  Inventory: {state.inventory}")
                log.info(f"  Score: {state.score}")

                # Create details row
                details_row = details_manager.create()
                details_row.step_id = step_id + 1
                details_row.plan = plan
                details_row.thought = thought
                details_row.action = action
                details_row.task = state.task
                details_row.feedback = state.feedback
                details_row.location = state.location
                details_row.description = state.description
                details_row.inventory = state.inventory
                details_row.score = state.score
                details_row.reward = reward
                details_row.is_done = is_done
                details_manager.add(details_row)

                # Handle end of episode
                if is_done:
                    break

                # Sleep for n seconds to avoid API throttling
                time.sleep(sleep_time)
                log.info("")

        except Exception as e:
            result_row.error = str(e)
            log.error(e)

        # Log the results
        log.info(f"Reward: {reward}")
        log.head("--- End of task ---\n")
        log.close()

        # Update result row
        total_sleep_time = sleep_time * (step_id + 1)
        result_row.stop_time = time.time()
        result_row.total_time = result_row.stop_time - result_row.start_time - total_sleep_time
        result_row.success = reward == 1.0
        result_row.reward = reward
        result_row.steps = step_id + 1
        result_row.max_steps = params.max_steps
        result_row.solution_steps = episode["solution_steps"]
        result_row.input_tokens = model.input_tokens
        result_row.output_tokens = model.output_tokens
        result_row.total_tokens = model.total_tokens
        result_row.input_cost = cost_calculator.get_input_cost(params.model_name, model.input_tokens)
        result_row.output_cost = cost_calculator.get_output_cost(params.model_name, model.output_tokens)
        result_row.total_cost = result_row.input_cost + result_row.output_cost
        result_row.reward_per_step = reward / (step_id + 1)
        result_row.reward_per_token = (reward / model.total_tokens) if model.total_tokens > 0 else 0.0
        results_manager.add(result_row)

        # Save the details
        details_manager.save()

        # Log the agent messages
        agent_writer.write(params, episode_id, agent.messages)

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

