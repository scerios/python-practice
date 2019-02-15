import random

# Display 10 random numbers from interval [0, 1). ")" show it will never return 1

for i in range(10):
    # random() ca be used to build customized random number generators
    print(random.random())


# Generate random numbert from interval [3, 7)
# Call random():                        [0, 1)
# Scale number(multiply by 4):          [0, 4)
# Shift number(add 3):                  [3, 7)

def rngNum():
    # random, scale, shift, return
    return 4 * random.random() + 3


for i in range(10):
    print(rngNum())

for j in range(10):
    print(random.uniform(3, 7))

# normalvariate() holds the numbers around the value of the first index
for k in range(20):
    print(random.normalvariate(5, 0.2))

# randint() generates a random whole number including both indexes
for h in range(20):
    print(random.randint(1, 6))
