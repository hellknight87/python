#This is the first program that I created fron the udemy tutorial
#Just a basic calculator, nothing more. Still learning the stuff.

import re

print("Our magical calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0 :

        equation = input("Enter equation:")
    else:
        equation = input(str(previous))


    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:() " "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
while run:
    performMath()
