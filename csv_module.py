# [C]omma [S]eparated [V]alue
#
# Title, Release year, Director
# The Godfather, 1972, Francis Ford Coppola
# The Shawshank Redemption, 1994, Frank Darabont
# Citizen Kane, 1941, Orson Welles

path = "C:\\Users\\Csirke\\greenfox\\Test Automation\\python-practice\\google_stock_data.csv"
file = open(path)
for line in file:
    print(line)

# Saving data in a list as lines
lines = [line for line in open(path)]
print(lines[0])

# Remove any leading or trailing whitespace
print(lines[0].strip())

# Division to smaller pieces
print(lines[0].strip().split(','))

dataset = [line.strip().split(',') for line in open(path)]
print(dataset[0])
print(dataset[1])