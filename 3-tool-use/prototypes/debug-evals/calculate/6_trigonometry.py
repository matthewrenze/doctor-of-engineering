# What is the result of math.sin(2 * math.pi/6) to six decimal places?
import math
expression = "round(sin(2 * pi/6), 6)"
result = eval(expression, {**math.__dict__}, {})
print(result)
assert result == 0.866025