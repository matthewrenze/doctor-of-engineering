# What is 2 to the power of 52?
import math
expression = "2**52"
result = eval(expression, {**math.__dict__}, {})
print(result)
assert result == 4503599627370496