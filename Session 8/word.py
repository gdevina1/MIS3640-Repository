fin = open('words.txt')
#line = fin.readline()
# print(line)

# fin = open('words.txt')
# for line in fin:
#     word = line.strip()
#     print(word)


# for line in fin:
#     word = line.strip()
#     if len(word)>20:
#         print(word)

def has_no_e(word):
    '''
    return True if the given word doesn't have the letter "e" in it
    '''
    # for letter in word:
    #     if letter == 'e':
    #         return False
    # return True
    return not 'e' in word.lower()

print(has_no_e('e'))
print(has_no_e('babson'))
print(has_no_e('EA'))

def find_words_no_e_percentage():
    counter_no_e = 0
    counter_total = 0
    for line in fin:
        counter_total += 1
        word = line.strip()
        if has_no_e(word):
            #print(word)
            counter_no_e += 1
    return counter_no_e/counter_total

# print('The percentage of the words with no "e" is {:.2f}%'.format(find_words_no_e_percentage()*100))

# def find_words_no_e():
#     for line in fin:
#         word = line.strip()
#         if has_no_e(word):
#             print(word)

def avoids(word, forbidden):
    for letter in word:
        for letter2 in forbidden:
            if letter == letter2:
                return False
    return True

print(avoids('Babson','abcd'))
print(avoids('College','ab'))

def find_words_no_vowels():
    counter_no_vowels = 0
    counter_total = 113809
    # print(counter_no_vowels)
    # fin = open('words.txt')
    for line in fin:
      #  counter_total += 1
        word = line.strip()
        
        # print(counter_total)
        
        if avoids(word,'aeiou'):
            print(word)
            counter_no_vowels += 1

    return counter_no_vowels/counter_total

print('The percentage of the words with no vowels is {:.2f}%'.format(find_words_no_vowels()*100))
