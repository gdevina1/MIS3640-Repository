def fibonacci(n):
    if n==1:
        return 1
    result = n + fibonacci (n-2)
    print("current n=",n)
    print("current n=", result)
    return result
    

print(fibonacci(12))