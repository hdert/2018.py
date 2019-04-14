'''
Author: Jsutin
Date Started: 21/08/2018
Date Now: 21/08/2018
'''

# -- Librarys --

from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import random

# -- Setup --

root = Tk()
root.title("Maze")
root.geometry("700x700+10+10")

# -- Classes --

class house:

    OLD = 'A old house'
    NON = 'A normal aged house'
    NEW = 'A new house'

    def __init__(self, hName, hAge, hLevel):
        self.name = hName
        self.age = hAge
        self.level = hLevel
        self.explored = False

    def __repr__(self):
        pass

# -- Variables --



# -- Functions --



# -- Frames --

f1 = Frame(root, width=300, height=200)

# -- Widgets --

st = ScrolledText(f1, state='disabled', bg='grey',
                  width=40, height=10, borderwidth = 3,
                  pady = 5)

# -- Code --

f1.place(x = 380, y = 10, anchor = N)

st.grid()

root.mainloop()
