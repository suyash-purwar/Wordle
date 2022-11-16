from customtkinter import *
from tkinter import *
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
        matrix.append(temp_matrix)
    
    return matrix

words = getRandomWord()
returnMatrix(words)

window = CTk(fg_color="#ffffff")
window.title("Word Puzzel Game")
# Default size  
# window.geometry(str(window.winfo_screenwidth()) + "x" + str(window.winfo_screenheight()))
# Minimum size
window.minsize(1500, 700)
# Add application icon
icon = PhotoImage(file='/home/suyash/Work/Programming/Tkinter/word-puzzel-game/assets/favicon.png')
window.tk.call('wm', 'iconphoto', window._w, icon)
# Set application theme
set_appearance_mode("light")

# Grid Configuration
window.grid_rowconfigure((1), weight=1)
window.grid_columnconfigure((0, 1), weight=1)

# Heading frame (Row 1)
app_header = CTkFrame(window, fg_color=None)
app_header.grid(row=0, column=0, columnspan=2, sticky="ns")

# Main heading (Children of Heading frame)
app_main_heading = CTkLabel(app_header, text="Word Puzzle Game", text_color="orange")
app_main_heading.configure(font=('Purisa', 35, 'bold'))
app_main_heading.grid(row=0, column=0, pady=25)

# Playground Frame (Row 2 Column 1)
playground = CTkFrame(window)
playground.grid(row=1, column=0, sticky="nsew")

playground_matrix = CTkFrame(playground, fg_color=None)
playground_matrix.pack()

# Dynamically create 10 by 10 matrix
for i in range(10):
    for j in range(10):
        CTkButton(playground_matrix, text=matrix[i][j], corner_radius=0, width=50, height=50, text_font=('Helvetica', 12), text_color="#ffffff", bg_color="#000000").grid(row=i, column=j, padx=5, pady=5)

# Words List (Row 2 Column 2)
playground_status = CTkFrame(window, fg_color="yellow")
playground_status.grid(row=1, column=1, sticky="nsew")

playground_status_heading = CTkLabel(playground_status, text="Find the following words: ", text_font=('Helvetica', 15))
playground_status_heading.grid(row=0, column=0, padx=10, pady=10)

word_check_var1 = StringVar()
word_check_var2 = StringVar()
word_check_var3 = StringVar()
word_check_var4 = StringVar()
word_check_var5 = StringVar()

word_checkbox_1 = CTkCheckBox(playground_status, text=words[0], command=lambda: print("pressed"), variable=word_check_var1, onvalue="on", offvalue="off")
word_checkbox_1.grid(row=1, column=0)
word_checkbox_2 = CTkCheckBox(playground_status, text=words[1], command=lambda: print("pressed"), variable=word_check_var2, onvalue="on", offvalue="off")
word_checkbox_2.grid(row=2, column=0)
word_checkbox_3 = CTkCheckBox(playground_status, text=words[2], command=lambda: print("pressed"), variable=word_check_var3, onvalue="on", offvalue="off")
word_checkbox_3.grid(row=3, column=0)
word_checkbox_4 = CTkCheckBox(playground_status, text=words[3], command=lambda: print("pressed"), variable=word_check_var4, onvalue="on", offvalue="off")
word_checkbox_4.grid(row=4, column=0)
word_checkbox_5 = CTkCheckBox(playground_status, text=words[4], command=lambda: print("pressed"), variable=word_check_var5, onvalue="on", offvalue="off")
word_checkbox_5.grid(row=5, column=0)

window.mainloop()