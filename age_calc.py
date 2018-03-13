#This will calculate a person's age
from datetime import datetime
my_date=input("Enter your date of birth in dd/mm/yyyy format:")
b_date = datetime.strptime(my_date, '%d/%m/%Y')

print ("Age : " % ((datetime.today()-b_date).days/365))
