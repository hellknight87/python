print("This program will get the name and age of a person and will print if it is time to retire or not")
name = input('Enter your name: ')
age = int(input('Enter your age: '))

if age <= 58:
	print('You may continue working', name)
else:
	print('Time to retire', name)
