import math

class CalculatorTool:

    def execute(self, expression: str) -> str:
        try:
            result = eval(expression, {**math.__dict__}, {})
            return str(result)
        except Exception as e:
            return f"Error: {str(e)}"


# # DEBUG:
# tool = CalculatorTool()
# result_1 = tool.execute("1 - min(1, 0.56 + 0.74)")
# print(result_1)