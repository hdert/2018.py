'''
Author: hdert
Date Started: 27/07/2018
Date Now: 27/07/2018
'''

# -- Librarys --

from tkinter import *
import random as rand
import string

# -- Setup --

root = Tk()
root.title("Password Generator")
root.geometry("700x700+10+10")
root.configure(bg = "lightgrey")

# -- Constant Lists --

adjectives = ['sleepy','slow','smelly', 'wet','fat','red','orange','yellow',
              'green','blue','purple','fluffy','white', 'proud', 'brave']

nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon','hammer',
         'duck', 'panda']

# -- Variables --

font = ("ariel", 14)
colour = "lightgrey"
adjective = adjectives[0]
noun = nouns[0]
number = 0

# -- Functions --

def display():
    global nouns
    global noun
    global adjectives
    global adjective
    global number
        
    adjective = rand.choice(adjectives)
    noun = rand.choice(nouns)
    number = rand.randrange(0, 100)
    char = rand.choice(string.punctuation)
    password.configure(text = '{}{}{}{}'.format(adjective, noun,
                                                   str(number), char))

# -- Widgets --

text = Label(root, text = "Password Generator", font = font, bg = 'black',
             fg = 'white')

password = Label(root, text = "Password Generator", bg = "grey",
                 font = ("ariel", 10))

btn = Button(root, text = 'Enter', command = display)

# -- Code --

text.pack()

password.pack()

btn.pack()

root.focus()
root.bind("<Return>", display)
root.mainloop()
