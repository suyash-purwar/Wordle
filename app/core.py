from random_word import RandomWords
import random as rand

r = RandomWords()

matrix = []

# Fetch five random words
def getRandomWord():
    words_list = []
    for i in range(5):
        word = r.get_random_word()
        while len(word) > 8:
            word = r.get_random_word()
        words_list.append(word)
    return words_list

def returnMatrix(words):
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    matrix_alphabets = []
    for w in words:
        # print(w)
        for alphas in w:
            matrix_alphabets.append(alphas.upper())

    rand.shuffle(matrix_alphabets)

    for i in range(100 - len(matrix_alphabets)):
        matrix_alphabets.append(alphabets[rand.randrange(26)])

    rand.shuffle(matrix_alphabets)

    index = 0
    for i in range(10):
        global matrix
        temp_matrix = []
        for j in range(10):
            temp_matrix.append(matrix_alphabets[index])
            index += 1
        print(temp_matrix)
        matrix.append(temp_matrix)
    
    return matrix

words = getRandomWord()
print(words)
returnMatrix(words)

