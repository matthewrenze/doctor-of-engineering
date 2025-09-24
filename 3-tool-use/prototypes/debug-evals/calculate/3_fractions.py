# What is the result of 10/3 to six decimal places?
import math
expression = "round(10/3, 6)"
result = eval(expression, {**math.__dict__}, {})
print(result)
assert f"{result:.6f}" == "3.333333"
