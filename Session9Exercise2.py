fin = open('words.txt')

# def is_abecedarian(word):
#     previous = word[0]
#     for c in word:
#         if c < previous:
#             return False
#         previous = c
#     return True

# print(is_abecedarian("bit"))
# print(is_abecedarian("cat"))


#--------REWRITE USING RECURSION-----------#

# def is_abecedarian(word):
#     count = 0 
#     if word[count]>word[count+1]:
#         return False
#     return is_abecedarian(word) idk
    

#--------REWRITE USING WHILE LOOPS-----------#
def is_abecedarian(word):
    count = 0
    while count < len(word) - 1:
        if word[count]>word[count+1]:
            return False
        count += 1
    return True

print(is_abecedarian("bit"))
print(is_abecedarian("cat"))