if len(input("Please enter a test string:")) < 6:
    print("Your string is too short.")
    print("Please enter a string with at least 6 characters!")

question = "How old are you?"
if len(input(question)) < 2:
    print("You must be at least 10 years old to fuck.")
else:
    print("You can fuck")
evenOrOdd = "Test a number if it's even or odd! Enter your number: "
number = int(input(evenOrOdd))

if number % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")

a = "The lenght of side a = "
aSide = int(input(a))
b = "The lenght of side b = "
bSide = int(input(b))
c = "The lenght of side c = "
cSide = int(input(c))
