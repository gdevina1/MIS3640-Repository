print("Session 4 - Functions")

#abstraction idea: do not need to know how a blackbox works to use it. all you need to know is where the input and output is
#function is an abstraction of a series of instructions
#decomposition idea: different devices work together to achieve an end goal

#decomposition - break problem into different, self-contained, pieces
#abstraction - suppress details of metod to compute something from use of that computation

#functions has a name, parameters, a docstring, and a body

################################################################################################################

#FUNCTION CALLS

print(type(42))
print(type(42.0))
print(type("hello"))
msg = "hello"
print(type(msg))
#"the function type takes argument and returns result"

print(int("42"))
#will show error cause it's not an int: print(int("hello"))
print(int(3.99))
print(int(-2.3))
print(float(3.14))
#will show error. to change str to a number, use float: print(int("3.14"))
print(str(42))
print(abs(-100))
#will show error cause abs takes only one argument: print(abs(-100, 42))
print(max(1,2))


#############################################################################################################

#MATH FUNCTIONS

# round(), min(), ord(), chr()

print(round(4.98778))
print(round(237.383333, 3)) #specifies the number of digits after the decimal point
#will show error cause cannot round multiple arguments print(round(9.29374, 6.99989))
print(min(3,9,0))
print(min(2918301, -9384758462191, 8, 78.2))
print(ord("a")) #ord prints out the unicode of the character
#will show error cause function can only take one argument print(ord("a", "b"))
#will show error cause function can only take string print(ord(2,284,97))

print(chr(97)) #chr prints out the corresponding character for the unicode. the inverse of ord
#will show error because funtion doesn't take multiple arguments print(chr(88, 39))
#will show error because function can only take ints print(chr("hj"))

print(isinstance(100, int))
print(isinstance(100.0, int))
print(type(100)==int)
print(type("hello")==str)

print(len("hello"))
#why doesnt this worrrkkkk???????????????print(len["s","d","f","k"])

#############################################################################################################3

#MORE MATH FUNCTIONS

import math
print(dir(math))

ratio = 100
print(math.log10(ratio))

degrees = 45
radians = degrees / 180.0 * math.pi # math.pi is just pi as in 3.14159265.....
print(math.sin(radians))

print(math.gamma(7))
print(math.gcd(2,8)) # can only take 2 arguments

###########################################################################################################

#Variables and Parameters


def print_twice(name_this):
    print(name_this)
    print(name_this)
  

print_twice("yahoo")

def cat_twice(part1, part2):
    cat = part1 + part2 #this variable is local so you can't use it outside the function
    print_twice(cat)

    
part1 = "Bing tiddle "
part2 = "tiddle bang."
cat_twice(part1,part2)

############################################################################################################

#Functions with returns and voids

def give_me_a_break():
    str1 = "break + kitkat"
    return str1 #return = "give me something back"

print(give_me_a_break())

#anything after the return function does not run. return has to be at the end of a function
def give_me_a_break():
    str1 = "break"  
    return str1
    print("another break") 

print(give_me_a_break()) 

#
def give_me_a_break():
    str1 = "break"
    print("another break")   
    return str1

print(give_me_a_break()) 

result = print_twice("bing")
print(result) 

##############################################################################################################

#EMPTY FUNCTION

#pass allows incomplete/empty functions to be ignored

def nop():
    pass

age= int(input())
if age >= 18:
    pass #without pass, you will see error.
    
############################################################################################################

#RETURN MORE THAN ONE VALUE

####NOOOTTTTT WORKINGGG????? BUT WORKS ON EXECUTOR

import math

def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

