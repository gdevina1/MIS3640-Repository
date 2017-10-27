print('Session 11- Dictionaries')

names = ['Rose', 'Jerry', 'Alex']
scores = [95, 75, 85]

grades = dict()
print(grades)

#list stores data, dictionaries do what?

grades['rose'] = 90
# creates an item that maps from the key 'Rose' to the value 90
print(grades)

grades ={'Rose': 90, 'Jerry': 75, 'Alex': 85}
print(grades)
# You might get different order of the key-value paris          ###idk what this means
# In general, the order of items in a dictionary is unpredictable.
print(grades['Jerry'])

# print(grades['Jason']) # there's no jason

print(len(grades)) # 3 keys

print('Jerry' in grades)
print('90' in grades) #only checks keys not values; will return False
print(90 in grades.values()) # check the values

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
h = histogram('Bookkeeper')
print(h)

number_of_e = h.get('e', 0)
number_of_a = h.get('a', 0)
print(number_of_e)
print(number_of_a)

def histogram(s):
    d = dict()
    for c in s.lower():
        d[c]= d.get(c, 0) + 1
    return d

h = histogram('Bookbookkeeper')
print(h)

def print_hist(h):
    for c in h:
        print(c, h[c])

h = histogram('Massachusetts')
print_hist(h)