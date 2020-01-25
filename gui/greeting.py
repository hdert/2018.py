'''
Author: hdert
Date Started: 24/07/2018
Date Now: 24/07/2018
'''

# -- Librarys --

from tkinter import *

# -- Setup --

root = Tk()
root.title("Greetings")
root.geometry("700x700+10+10")
root.configure(bg = "lightgrey")

# -- Constant Lists --

CHOICES = ["lightgrey", "grey", "white", "darkgrey"]

# -- Variables --

choice = StringVar()
choice.set(CHOICES[0])
colour = "lightgrey"
font = ("ariel", 14)

# -- Functions --

def name():
    pass

def update():
    global colour
    colour = choice.get()
    root.configure(bg = colour)
    text.configure(bg = colour)
    text2.configure(bg = colour)

# -- Widgets --

text = Label(root, text = "Greeting", bg = colour, font = font)
text2 = Label(root, text = "Hello ________", bg = colour, font = font)
btn = Button(root, text = "Enter", command = name)
em = OptionMenu(root, choice, *CHOICES)
btn2 = Button(root, text = "Update", command = update)

# -- Code --

text.grid(row = 0, column = 1, sticky = N+S+E+W)

text2.grid(row = 1, column = 1)

btn.grid(row = 2, column = 1, sticky = N+S+E+W)
btn.bind("<Return>", update)

em.grid(row = 3, column = 1, sticky = N+S+E+W)
em.focus()
em.bind("<Return>", update)

btn2.grid(row = 4, column = 1, sticky = N+S+E+W)

root.mainloop()
