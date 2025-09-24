# What is the determinant of the matrix [[12, 7, 3], [ 4, 5, 6], [ 7, 8, 9]] rounded to the nearest integer?
import numpy as np
matrix = np.array([[12, 7, 3], [4, 5, 6], [7, 8, 9]])
determinant = np.linalg.det(matrix)
rounded_determinant = round(determinant)
print(rounded_determinant)