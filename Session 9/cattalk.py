fin = open('words.txt')

def cartalk():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        for counter in range(1, len(word)-5):
            if word[counter]==word[counter+1] and word[counter+2]==word[counter+3] and word[counter+4]==word[counter+5]:
                print(word)
            

   


