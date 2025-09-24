# What is the result of (7 - (2 + 3)) * (4 - 1)?
import math
expression = "(7 - (2 + 3)) * (4 - 1)"
result = eval(expression, {**math.__dict__}, {})
print(result)
assert result == 6