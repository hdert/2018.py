'''
Author: hdert
Date Start: 05/07/2018
Date Now: 05/07/2018
Version: V 0.1.2.3.5 Dev
'''

#--Librarys

import random as rand
from tkinter import *

#--Setup--

root = Tk()
root.title("Guessing Game")
root.geometry("700x700+10+10")
root.configure(bg = "lightgrey")

#--Lists--

SET = ["Easy", "Medium", "Hard"]

#--Variables--

customFont = ("ariel", 12)
color = "lightgrey"
rand_ = 0
setup = False
name = ""
guesses = 0
trip = False
input_ = 0
usrGuess = 0
place = StringVar()
place.set(SET[0])
maxG = 0

#--Definitions--

def guess(event = None):
    global rand_
    global setup
    global name
    global guesses
    global trip
    global input_
    global usrGuess
    global maxG
    if setup == False:
        rand_ = hardness()
        name = en.get()
        setup = True
        msgBox.configure(text = "Please Enter A Number")
        diff.destroy()
    else:
        trip = False
        try:
            input_ = en.get()
            usrGuess = int(input_)
        except:
            msgBox.configure(text = "That's Not A Number")
            guesses += 1
            trip = True
        if usrGuess <= 0 and trip == False:
            msgBox.configure(text = "Try Putting In A Number In Between 0 And {}".format(maxG + 1))
            guesses += 1
            trip = True
        elif usrGuess > maxG and trip == False:
            msgBox.configure(text = "Try Putting In A Number In Between 0 And {}".format(maxG + 1))
            guesses += 1
            trip = True
        if usrGuess == rand_ and trip == False:
            msgBox.configure(text = "You Guessed Right\nIt Took You {} Trys".format(guesses))
            text_.configure(text = "Thanks For Playing {}".format(name), bg = "green")
            root.configure(bg = "Green")
        elif usrGuess > rand_ and trip == False:
            msgBox.configure(text = "You Guessed To High")
            guesses += 1
        elif usrGuess < rand_ and trip == False:
            msgBox.configure(text = "You Guessed To Low")
            guesses += 1
    en.delete(0, END)

def hardness():
    global maxG
    sel = place.get()
    
    if sel == "Easy":
        maxG = 100
        return (rand.randint(1, 100))
    elif sel == "Medium":
        maxG = 500
        return (rand.randint(1, 500))
    elif sel == "Hard":
        maxG = 2000
        return (rand.randint(1, 2000))
    
#--Widgets--

text_ = Label(root, text = "This Is My Guessing Game",
              font = customFont, bg = color)

diff = OptionMenu(root, place, *SET)

en = Entry(root, bg = color)

btn = Button(root, text = "Enter", command = guess)

msgBox = Label(root,
               text = "Please Choose A Difficulty\nAnd Write Your Name In The Entry Box",
               font = ("ariel", 10), bg = "grey")

#--Extras--

text_.pack()

diff.pack()
diff.configure(bg = color)

en.pack()
en.focus()
en.bind("<Return>", guess)

btn.pack()

msgBox.pack()

root.mainloop()
