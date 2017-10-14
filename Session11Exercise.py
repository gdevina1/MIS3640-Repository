fin = open('words.txt')

# def dictionary(words):
#     words = open('words.txt')
#     d = {}
#     for line in words:
#         words[line] = line 
#     return words
# d = dictionary('words.txt')
# print(d)
#idk what im doing



def has_duplicates(list_one):
    d = {}
    for s in list_one:
        d[s] = 1 + d.get(s, 0)
        if d[s] > 1:
            return True
        else:
            return False

list_one = ['gianca', 'is', 'way', 'way', 'cool']

print (has_duplicates(list_one))
#whyyyy i h8 this
