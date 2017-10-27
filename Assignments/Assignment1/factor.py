def factor(n):
    '''
    Question: Write a program that asks the user for an integer and then prints out all its factors. 
    For example, when the user enters 150, the program should print 2 3 5 5
    '''
    '''
    Function factor takes integer n and returns a list of n's prime factors using nested while loops that continues 
    to run if n is greater than 1 is still true after dividing n by x indexes starting from 2 that gives 
    no remainders. The inner loop allows n to be replaced by a smaller number of n/x given that n is divisible by x.
    '''
    x = 2                       #starts count at 2 so 1 is not included in the answer
    p_factors = []              #all the resulting prime factors from the function will be put in a list
    while n > 1:                #keeps function running if n is greater than 1
        while n % x == 0:       #keeps function running if n divided by the index has no remainder, which means n is divisible by x index
            n = n/x             #if so, then n is to be divided by x 
            p_factors.append(x) #x is to be added to list of results           
        x += 1                  #increases index x by 1 every loop
    return p_factors            #returns the list of prime factors of integer n

n = int(input('Please enter an integer: ')) 
print(factor(n))                           