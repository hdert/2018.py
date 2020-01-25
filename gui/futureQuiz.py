'''
Author: hdert
Date Started: 25/07/2018
Date Now: 25/07/2018
'''

# -- Librarys --

import random as rand
from tkinter import *

# -- Setup --

root = Tk()
root.title("Questions")
root.geometry("700x700+10+10")
root.configure(bg = "lightgrey")

# -- Constant Lists --

animals = ['tiger', 'giraffe', 'elephant', 'hippo', 'wolf']
questions = {'tiger':'Stripy Desert Animal', 'giraffe':'Holds Head Very High',
           'elephant': 'A Giant Beast', 'hippo':'Have You Ever Seen It\'s Bowl Movement?',
           'wolf':'A Stealthy Preadator'}

# -- Variables --

colour = "lightgrey"
font = ("ariel", 14)

# -- Functions --

def check():
    pass

# -- Widgets --

text = Label(root, text = "Welcome To My Guessing Game\nPlease Enter Your Name Below", bg = colour, font = font)
en = Entry(root, bg = colour)
msgBox = Label(root, text = "msgBox", bg = "darkgrey", font = ("ariel", 10))
btn = Button(root, text = "Enter", command = check)

# -- Code --

text.grid()
en.grid()
msgBox.grid()
btn.grid()


root.mainloop()
