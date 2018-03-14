import re

print("Our magical calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():

    equation = input("Enter equation:")
    if equation == 'quit':
        run = False
    else:
        print("You typed", equation)

while run:
    performMath()