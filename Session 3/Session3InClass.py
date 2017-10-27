print("Data Types")

#numbers --------------------------------------------------------------------------------------------
print("3.14e-2") # scientific notation

print("123 + 222") # integer addition

print("1.5 * 4") # floating-point multiplication

print("2 ** 100") # 2^100

print("len(str(2 ** 1000000))") # How many digits in a really BIG number? 
# it has to be str because len doesn't allow fors ints to be counted

import math
print(math.pi)
print(math.sqrt(69))

import random
print(random.random())
print(random.choice([1, 2, 3, 4])) #you have to give a selection

#----------------------------------------------------------------------------------------------------------------------

#Strings

print("I\'m \"ok\".") #backslash tells code that any character that comes after it is not the closing character

print('I\'m learning\nPython.') #\n is for next line

print('\\\n\\')

print('\\n') #\\ shows a \

print(r'\\\n\\') #r can be used to disable the escape \ character

print('''line1 ... 
line2 ... 
line3''')

#-------------------------------------------------------------

#Boolean

print(True)
print(False)

print(3>1)
#True

print(1>2)
#false

print(True and True)
#true

print(True and False)
#false

print(False and False)
#false

print(5>3 and 3>1)
#true

print(True or True)
#true

print(True or False)
#true

print(False or False)
#False

print(5>3 or 1>3)
#true

print(not True)
#False

print(not False)
#True 

print(not 1>2)
#true






