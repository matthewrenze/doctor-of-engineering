# How many different ways are there to choose 24 objects from a set of 51?
import math
expression = "comb(51, 24)"
result = eval(expression, {**math.__dict__}, {})
print(result)
assert result == 229591913401900