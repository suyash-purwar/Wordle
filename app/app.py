from customtkinter import *
from tkinter import *
from random_word import RandomWords
import random as rand

BTN_COLOR = "#3B8ED0"
BTN_COLOR_HOVER = "#36719F"
BTN_COLOR_DISABLED = "#d4d4d4"

r = RandomWords()

matrix = []

# Fetch five random words
def getRandomWord():
    words_list = []
    for i in range(5):
        word = r.get_random_word()
        while len(word) > 8:
            word = r.get_random_word()
        words_list.append(word.upper())
    return words_list

def returnMatrix(words):
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    matrix_alphabets = []
    for w in words:
        for alphas in w:
            matrix_alphabets.append(alphas)

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
window.geometry(str(window.winfo_screenwidth()) + "x" + str(window.winfo_screenheight()))
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
playground = CTkFrame(window, fg_color=None)
playground.grid(row=1, column=0, sticky="nsew")

playground_matrix = CTkFrame(playground, fg_color=None)
playground_matrix.pack()

swap_btn = CTkButton(playground, text="SWAP", text_color="#ffffff", fg_color=BTN_COLOR_DISABLED, state=DISABLED, text_font=('Helvetica', 13), height=50)
swap_btn.pack(side=LEFT, padx=250, pady=0)

check_btn = CTkButton(playground, text="CHECK", fg_color=BTN_COLOR_DISABLED, state=DISABLED, text_color="#ffffff", text_font=('Helvetica', 13), height=50)
check_btn.pack(side=LEFT, padx=0, pady=0)

matrix_btn_array = []
clicked=[]
def matrix_tile_clicked(coordinate):
    coordinate = (int(coordinate.split()[0]), int(coordinate.split()[1]))

    # Check if the incoming coordinate is directly adjacent to previous coordinate
    if len(clicked):
        prev = clicked[len(clicked)-1]
        print(prev[0], prev[1])
        if ((coordinate[0] in range(prev[0]-1, prev[0]+2) and prev[1] == coordinate[1]) or (coordinate[1] in range(prev[1]-1, prev[1]+2) and prev[0] == coordinate[0])):
            print(coordinate in clicked)
            if coordinate in clicked:
                # If present in the clicked list
                clicked.remove(coordinate)
                for btn in matrix_btn_array:
                    if (btn.coordinate == coordinate):
                        print(btn.coordinate)
                        btn.configure(fg_color=BTN_COLOR)
            else:
                clicked.append(coordinate)
                for btn in matrix_btn_array:
                    if (btn.coordinate == coordinate):
                        print(btn.coordinate)
                        btn.configure(fg_color=BTN_COLOR_HOVER)
        else:
            print("Selection not allowed!")
    else:
        clicked.append(coordinate)
        for btn in matrix_btn_array:
            if (btn.coordinate == coordinate):
                print(btn.coordinate)
                btn.configure(fg_color=BTN_COLOR_HOVER)

    if (len(clicked) == 2):
        swap_btn.configure(state=NORMAL)
        swap_btn.configure(fg_color=BTN_COLOR)
    else:
        swap_btn.configure(state=DISABLED)
        swap_btn.configure(fg_color=BTN_COLOR_DISABLED)

    if (len(clicked) >= 2):
        check_btn.configure(state=NORMAL)
        check_btn.configure(fg_color=BTN_COLOR)
    else:
        check_btn.configure(state=DISABLED)
        check_btn.configure(fg_color=BTN_COLOR_DISABLED)
    
    print(clicked)

def swap_tiles():
    if len(clicked) <= 2:
        # Do stuff
        print("Enabled")

# Dynamically create 10 by 10 matrix
for i in range(10):
    for j in range(10):
        btn = CTkButton(playground_matrix, text=matrix[i][j], corner_radius=0, width=50, height=50, text_font=('Helvetica', 12), text_color="#ffffff", bg_color="#000000", command = lambda m = str(i)+' '+str(j):matrix_tile_clicked(m))
        btn.grid(row=i, column=j, padx=5, pady=5)
        btn.coordinate=(i, j)
        matrix_btn_array.append(btn)

# Words List (Row 2 Column 2)
playground_status = CTkFrame(window, fg_color=None)
playground_status.grid(row=1, column=1, sticky="nsew")

playground_status_heading = CTkLabel(playground_status, text="Swap the alphabets to make following words: ", text_font=('Helvetica', 20), height=70)
playground_status_heading.pack(padx=(20, 0), pady=(5, 10), anchor=W)

word_check_var1 = StringVar()
word_check_var2 = StringVar()
word_check_var3 = StringVar()
word_check_var4 = StringVar()
word_check_var5 = StringVar()

word_checkbox_1 = CTkCheckBox(playground_status, text=words[0], command=lambda: print("pressed"), variable=word_check_var1, onvalue="on", offvalue="off", text_font=('Helvetica', 15), corner_radius=15, border_width=2, text_color_disabled="#000000", state=DISABLED)
word_checkbox_1.pack(padx=(50, 0), pady=10, anchor=W)
word_checkbox_2 = CTkCheckBox(playground_status, text=words[1], command=lambda: print("pressed"), variable=word_check_var2, onvalue="on", offvalue="off", text_font=('Helvetica', 15), corner_radius=15, border_width=2, text_color_disabled="#000000", state=DISABLED)
word_checkbox_2.pack(padx=(50, 0), pady=10, anchor=W)
word_checkbox_3 = CTkCheckBox(playground_status, text=words[2], command=lambda: print("pressed"), variable=word_check_var3, onvalue="on", offvalue="off", text_font=('Helvetica', 15), corner_radius=15, border_width=2, text_color_disabled="#000000", state=DISABLED)
word_checkbox_3.pack(padx=(50, 0), pady=10, anchor=W)
word_checkbox_4 = CTkCheckBox(playground_status, text=words[3], command=lambda: print("pressed"), variable=word_check_var4, onvalue="on", offvalue="off", text_font=('Helvetica', 15), corner_radius=15, border_width=2, text_color_disabled="#000000", state=DISABLED)
word_checkbox_4.pack(padx=(50, 0), pady=10, anchor=W)
word_checkbox_5 = CTkCheckBox(playground_status, text=words[4], command=lambda: print("pressed"), variable=word_check_var5, onvalue="on", offvalue="off", text_font=('Helvetica', 15), corner_radius=15, border_width=2, text_color_disabled="#000000", state=DISABLED)
word_checkbox_5.pack(padx=(50, 0), pady=10, anchor=W)

word_checkbox_3.select(1)

window.mainloop()