def print_lyrics():
    print("Hey Jude. Don't make it bad.")

print("Take a sad song and make it better.")

print_lyrics()

print(type(print_lyrics))

def repeat_lyrics():
    print_lyrics()
    print('Na - na - na - na - na, na - na - na - na')
    print_lyrics()

# repeat_lyrics()

def print_twice(name):
    print(name)
    print(name)

print_twice("Gianca")

my_name = "Gi"
print(my_name)

#printing
def my_abs(number):
    print(abs(number))

my_abs(-626) 

#returning
def my_abs(number):
    return abs(number)

print(my_abs(-10))

#argument checking
def my_abs(number):
    if isinstance(number,(int,float)) == True:
        return abs(number)

    else:
        print("not an int or a float")

print(my_abs("sj"))
print(my_abs(-0.397))

#prof's solution
def my_abs(n):
    if isinstance(n, int) or isinstance(n, float):
        if n <= 0:
            pass
            #to be continued

