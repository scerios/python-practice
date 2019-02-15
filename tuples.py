import sys
import timeit

# List -add, -remove, -change
primes = [2, 3, 5, 7, 11, 13, 17]

# Tuple is FINAL
squaresOfTwo = (2, 4, 8, 16, 32, 64)

print("Primes:", len(primes))
print("Squares:", len(squaresOfTwo))

for i in primes:
    print("Prime:", i)

for i in squaresOfTwo:
    print("Square:", i)

list = [2, "kys", True, 1.5]
tuple = (2, "kys", True, 1.5)

# How much memory does it use
print("List:", sys.getsizeof(list))
print("List:", sys.getsizeof(tuple))
