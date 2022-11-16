from customtkinter import *
from tkinter import *

window = CTk()
window.title("Word Puzzel Game")
# Default size  
window.geometry(str(window.winfo_screenwidth()) + "x" + str(window.winfo_screenheight()))
# Minimum size
window.minsize(1500, 700)
# Add application icon
icon = PhotoImage(file='/home/suyash/Work/Programming/Tkinter/word-puzzel-game/assets/favicon.png')
window.tk.call('wm', 'iconphoto', window._w, icon)



window.mainloop()