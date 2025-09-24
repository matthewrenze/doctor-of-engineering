# What is the definite integral of 1/x from x = 1 to x = e?
import math
expression = "log(e) - log(1)"
result = eval(expression, {**math.__dict__}, {})
print(result)
assert result == 1.0