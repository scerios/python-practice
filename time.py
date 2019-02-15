import datetime

a = 5
print(a)
b = 2
a = b
print(a)
print(a == b)

today = datetime.date(1989, 10, 6)
print(today)

delta = datetime.timedelta(500)
print(today + delta)

print(today.strftime("%A, %B, %d, %Y"))
birthday = "I was born on {:%A, %B, %d, %Y}."
print(birthday.format(today))

bestDayOfMyLife = datetime.date(2007, 3, 24)
bestTimeOfMyLife = datetime.time(22, 14, 38)
best = datetime.datetime(2007, 3, 24, 22, 14, 38)

print(bestDayOfMyLife)
print(bestTimeOfMyLife)
print(best)
print(datetime.datetime.today())
