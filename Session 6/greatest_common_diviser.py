def gcd(a,b):
    if a == b:
        return a
    elif a == 0:
        return 0
    elif b == 0:
        return 0
    elif a > b:
        return a % b
    elif b > a:
        return b % a
    else:
        print("IDK WHAT IM DOING. PLS STOP IT WITH THE MATH.")
    #if a > b:
    # a,b = b,a
    # for x in range (a, 0, -1)
    # return x


print(gcd(12,12))
print(gcd(0,12))
print(gcd(12,0))
print(gcd(9,12))
print(gcd(17,12))
