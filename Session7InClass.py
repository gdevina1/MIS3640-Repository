print("Session 7 - ")
#Exercise 1
#1
result = 0
for i in range (10):
    result = result + (i + 1)
    #print("in the {}th iteration, result = {}".format(i, result))

#2
result = 0
for i in range (1000):
    result = result + (i + 1)
    #print("in the {}th iteration, result = {}".format(i, result))

#all dem mods from 1-10
result = 1
for i in range (10):
    result = result * (i + 1)
    #print("in the {}th iteration, result = {}".format(i, result))

#3 - sum of all odd numbers
result = 0
for i in range (1, 1000, 2): #range(start,stop,step)
    result = result + (i + 1)
    print("in the {}th iteration, result = {}".format(i, result))

#3.b - sum of all even numbers
result = 0
for i in range (0, 1001, 2): #range(number is not inclusive of if you just specify 1000, 1000 won't be included in the calculation)
    result = result + (i + 1)
    print("in the {}th iteration, result = {}".format(i, result))

for c in "hello":
    print(c)

for gianca in ["hello", "world", "eff", "off"]: #use square brackets, it's for LISTS
    print(gianca)


##################################################################################################################

#THE WHILE STATEMENT

# def countdown(n):
#     while n>0:
#         print(n)
#         n = n - 1
#     print("Blastoff!")

# countdown(10)

# iteration = 0
# count = 0
# while iteration < 5:
#     # the variable 'letter' in the loop stands for every 
#     # character, including spaces and commas!
#     for letter in "hello, world": 
#         count += 1 #+= is same as count = count +1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break #this stops the iteration
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)

print('Done!')

