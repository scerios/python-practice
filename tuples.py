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

# How much time does it take to make
listTime = timeit.timeit(stmt="[1,2,3,4,5]", number=10000000)
tupleTime = timeit.timeit(stmt="(1,2,3,4,5)", number=10000000)

print("Time to make list:", listTime)
print("Time to make tuple:", tupleTime)

empty_tuple = ()
# Tuple with 1 value is just a string
test0 = ("a")
test1 = ("a",)
test2 = ("a", "b")
test3 = ("a", "b", "c")

print(empty_tuple)
print(test0)
print(test1)
print(test2)
print(test3)

# Another way to instanciate a tuple
test4 = 1,
test5 = 1, 2
test6 = 1, 2, 3

print(test4)
print(test5)
print(test6)
