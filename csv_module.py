import csv
from datetime import datetime

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

path_csv = "C:\\Users\\Csirke\\greenfox\\Test Automation\\python-practice\\google_stock_data.csv"
file_csv = open(path_csv, newline='')
reader = csv.reader(file_csv)

# First line is a header
header = next(reader)
# Read the remaining data
data = [row for row in reader]
print(header)
print(data[0])

# Separating data values
info = []
for row in reader:
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])
    info.append([date, open_price, high, low, close, volume, adj_close])

print(info[0])
