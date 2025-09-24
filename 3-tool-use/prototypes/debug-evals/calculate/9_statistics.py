# What is the result of math.erf(1.96/math.sqrt(2)) to two decimal places?
import math
expression = "round(erf(1.96/sqrt(2)), 2)"
result = eval(expression, {**math.__dict__}, {})
print(result)
assert result == 0.95
