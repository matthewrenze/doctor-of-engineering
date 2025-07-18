# Import packages
from models.model_factory import ModelFactory
from evals.eval_factory import EvalFactory
from prompts.prompt_factory import PromptFactory
from graders.grader_factory import GraderFactory

# Set parameters
model_name = "gpt-4.1"
eval_name = "if-eval-10"
strength_id = "baseline"
instruction_id = "exclude-letter-e"

# Create components
model_factory = ModelFactory()
prompt_factory = PromptFactory()
eval_factory = EvalFactory()

# Create entities
eval = eval_factory.create(eval_name)
task_count = len(eval)

score = 0
for task_id in range(task_count):

    # Get the task
    task = eval[task_id]

    # Create entities
    model = model_factory.create(model_name)
    prompt = prompt_factory.create(task, instruction_id, strength_id)
    grader = GraderFactory().create(instruction_id)

    # Get the response
    response = model.get_response(prompt)
    response = response.replace("\n\n", "\n")

    # Grade the response
    grade = grader.grade(response)
    if grade:
        score += 1

    # Print the result
    print(f"Task ID: {task_id}")
    print(f"System Prompt: {prompt.system_prompt}")
    print(f"Example Prompt: {prompt.example_prompt}")
    print(f"Example Response: {prompt.example_response}")
    print(f"User Prompt: {prompt.user_prompt}")
    print(f"Response: {response}")
    print(f"Grade: {grade}")
    print()

print(f"Tasks: {task_count}")
print(f"Accuracy: {score}/{task_count}")

