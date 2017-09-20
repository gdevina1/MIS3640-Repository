def factorial(n):
    result = 1
    if n==1:
        return 1
    result = n * factorial (n-1)
    print("current n=",n)
    print("current n=", result)
    return result
    

print(factorial(12))