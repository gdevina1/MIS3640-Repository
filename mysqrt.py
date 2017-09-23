import math

epsilon = 0.0000001

def mysqrt(a):
    x = a + 4
    while True:
        y = (x + (a/x)) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return y

def text_square_root():
    print("a         ", "mysqrt(a)             ", "math.sqrt(a)             ", "diff     ")
    print("_          ____________           ___________________     ____________________")
    print("")
    for a in range (1,10):
        n = float(a)
        s = str(mysqrt(a))
        r = str(math.sqrt(a))
        d = abs(math.sqrt(a) - mysqrt(a))
        if len(s) == 17:
            print(n,"      ",s,"    ",r,"     ",d)
        elif len(s) == 18:
            print(n,"      ",s,"   ",r,"    ",d)
        elif len(s) == 16:
            print(n,"      ",s,"     ",r,"      ",d)
        elif len(s) == 3:
            print(n,"      ",s,"                  ",r, "                   ", d)
            


print(text_square_root())

        

