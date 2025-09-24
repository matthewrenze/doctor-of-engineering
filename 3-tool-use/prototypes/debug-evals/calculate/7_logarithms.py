# What is log base 3 of 81?
import math
expression = "log(81, 3)"
result = eval(expression, {**math.__dict__}, {})
print(result)
assert result == 4.0