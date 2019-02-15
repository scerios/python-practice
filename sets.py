# Array (unordered)
example = set()

example.add(42)
example.add(True)
example.add("Diamond")
print(example)
print(len(example))

example.remove("Diamond")
print(len(example))

# Safe remove
example.discard(6)

# Empty the set
# example.clear()

odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])
print(odds.union(evens))
print(odds.intersection(primes))
print(evens.union(evens))
print(evens.union(example))
