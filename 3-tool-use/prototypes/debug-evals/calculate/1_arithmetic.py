# What is the result of 2 + 3 * 4 - 5?
import math
expression = "2 + 3 * 4 - 5"
result = eval(expression, {**math.__dict__}, {})
print(result)
assert result == 9