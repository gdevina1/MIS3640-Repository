print("Session 6 - Conditionals")
    
age = input ("What is your age?")
age= int(age)

#Chained Conditionals
if age >= 18:
    print("Your age is {}".format(age))
    print("Adult")
elif age >=6:
    print("Your age is {}".format(age))
    print("Teenage")
else:
    print("cudi the kid")

age = 20
if age >= 6:
    print("teenager")
elif age >= 18:
    print("adult")
else:
    print("kid")

#Recursion

import time
def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        time.sleep(1)
        countdown(n-1)

countdown(6)