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
