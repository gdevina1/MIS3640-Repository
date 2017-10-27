#exercise 4


#1
def price(word):
    
    p = 0
    for letter in word:
        p += ord(letter)-96
    return p

print('bananas', '      $',price('bananas'))
print('rice', '         $',price('rice'))
print('paprika', '      $',price('paprika'))
print('potato chips', ' $',price('potato chips'))
print('--------------------')
print('Total','        $', price('bananas') + price('rice') + price('paprika') + price('potato chips'))

#2
print('{:13} {:1} {:6}'.format('bananas','$','52.00'))
print('{:13} {:1} {:6}'.format('rice',     '$','35.00'))
print('{:13} {:1} {:6}'.format('paprika',  '$','72.00'))
print('{:13} {:1} {:6}'.format('potato chips',  '$','78.00'))
print('---------------------')
print('{:12} {:1} {:6}'.format('Total', '$','237.00'))

#3
#:(


