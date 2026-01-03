import os
import json
from common.parameters import Parameters


class DialogueWriter:

    def write(self, params: Parameters, episode_id: int, step_id: int, subagent: str, messages: list):

        # Create the folder
        folder_path = f"../data/messages/{params.agent_name} - {params.model_name} - {params.eval_name}"
        os.makedirs(folder_path, exist_ok=True)

        # Write the messages
        file_path = f"{folder_path}/{episode_id}-{step_id}-{subagent}.jsonl"
        with open(file_path, "w") as f:
            for message in messages:
                json_text = json.dumps(message)
                f.write(f"{json_text}\n")

if __name__ == "__main__":
    params = Parameters(
        agent_name="test_agent",
        model_name="test_model",
        env_name="test_env",
        eval_name="test_eval",
        max_steps=10
    )
    messages = [
        {"role": "system", "content": "system prompt goes here"},
        {"role": "user", "content": "user prompt goes here"},
        {"role": "assistant", "content": "assistant response goes here"},
    ]
    writer = DialogueWriter()
    writer.write(params, 0, messages)




