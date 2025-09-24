# What is the sum of the ASCII values of the characters in the string 'hello world!'?
input_string = 'hello world!'
ascii_values = [ord(char) for char in input_string]
ascii_sum = sum(ascii_values)
print(ascii_sum)