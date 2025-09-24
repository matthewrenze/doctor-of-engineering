# What is the md5 hash (hex digest) of the string "Hello, Agent!"?
import hashlib
input_string = "Hello, Agent!"
md5_hash = hashlib.md5(input_string.encode()).hexdigest()
print(md5_hash)