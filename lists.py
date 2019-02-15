# Arraylist (ordered)
example = list()
anotherExample = []

primes = [2, 3, 5, 7, 11, 13]
primes.append(17)
primes.append(19)

print(primes)
print(primes[2])
print(primes[2] + primes[0])
print(primes[-1])

# Slicing
print(primes[2:5])

# Multi-value list
everything = [6, True, "RL", ["Diamond", True, 29]]
print(everything)

# Concatenation
numbers = [1, 2, 3]
letters = ["a", "b", "c"]
print(numbers + letters)
print(letters + numbers)
print(numbers + numbers)
