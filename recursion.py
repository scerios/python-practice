# [L]east [R]ecently [U]sed Cache
from functools import lru_cache


# Bad and slow example
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


for n in range(1, 101):
  print(n, ":", fibonacci(n))

# Memoization
fibonacciCache = {}


def fibonacciMemo(i):
    # If we have cached the value, then return it
    if i in fibonacciCache:
        return fibonacciCache[i]

    # Compute the Nth term
    if i == 1:
        save = 1
    elif i == 2:
        save = 1
    elif i > 2:
        save = fibonacciMemo(i - 1) + fibonacciMemo(i - 2)

    # Cache the value an return it
    fibonacciCache[i] = save
    return save


for i in range(1, 1001):
    print(i, ":", fibonacciMemo(i))


@lru_cache(maxsize=1000)
def fibonacciLRU(j):
    # Chech if the input is a positive integer (throw)
    if type(j) != int:
        raise TypeError("j must be a positive int")
    if j < 1:
        raise ValueError("j must be a positive int")

    if j == 1:
        return 1
    elif j == 2:
        return 1
    elif j > 2:
        return fibonacciLRU(j - 1) + fibonacciLRU(j - 2)


for j in range(1, 501):
    print(j, ":", fibonacciLRU(j))
