print("Session 8 - Strings")

team = "New England Patriots"

# letter = team[-1]

# print(letter)

# print(team[len(team)-1])
# print(team[-2])

# # index = 0
# # for i in range(len(team)):
# #     if team[i] != " ":
# #         print(team[i])


# # for letter in team:
# #     print(letter)

# for letter in team:
#     if letter.isalpha():
#         print(letter)

# prefixes = "JKLMNOQP"
# suffix = "ack"
# for letter in prefixes:
#     # if letter == "O" or  letter == "Q":
#     #     print(letter + "u" + suffix)
#     # else:
#     #     print(letter + suffix)
#     if letter in ["O","Q"]:
#         letter = letter + "u"
#     print(letter + suffix)


######################################
######### S L I C I N G ##############
######################################

# print(team[0:11]) #non inclusive, only til character 10
# print(team[:11])
# print(team[12:])
# print(team[::-1])
# print(team[::-2])
# print(team[4:3]) #spits out nothing
# print(team[4:0]) #spits out nothing
# print(team[::2])

############################################################

# team = "New England Patriots"
# #team [12:20] = "Seahawks" #this don't work

# new_team = (team[:12]) + "Beavers"
# print(new_team)

##############################################################

# def find(word,letter):
#     index = 0
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index = index + 1
#     return -1

# print(find(team,"a"))
# print(find(team,"W"))

# word = "New England Patriots"
# count = 0
# for letter == "a":
#     if letter == "a":
#         count = count +1
# print(count)

team = "New England Team"

def count(word, letter):
    word = word.lower()
    c = 0
    for x in word:
        if x == letter.lower():
            c = c + 1
    return c

print(count(team,"n"))

vowels = "aeiou"
number_of_vowels = 0
for letter in vowels:
    number_of_vowels += count(team, letter)

print(number_of_vowels)

def in_both(word1,word2):
    for letter in word1:
        if letter in word2:
            print(letter)

in_both("fart","bart")