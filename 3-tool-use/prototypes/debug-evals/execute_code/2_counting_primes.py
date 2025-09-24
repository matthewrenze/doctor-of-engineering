# How many prime numbers are there between 1 and 100,000 inclusive?
import sympy
primes = list(sympy.primerange(1, 100001))
print(len(primes))
