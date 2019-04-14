'''
Author: Justin
Date Started: 16/07/2018
Date Now: 16/07/2018
Version: V 0.1.1.1.1 Dev
'''

#--Librarys--

from tkinter import *
import random as rand

#--Setup--

root = Tk()
root.title("Dice")
root.geometry("700x700+10+10")
root.configure(bg = "lightgrey")

#--Lists--

OPTIONS = ["6", "10", "15", "30"]

#--Variables--

customFont = ("ariel", 14)
sides = StringVar()
sides.set(OPTIONS[0])
countW = 0
countT = 0
currState = ""

#--Functions--

def dice():
    global sides
    global countW
    global countT
    global currState
    set_ = int(sides.get())
    num = rand.randint(0, set_)
    roll = rand.randint(0, set_)
    if num == roll:
        currState = "Win"
        countW += 1
        countT += 1
    else:
        currState = "Lose"
        countT += 1
    msgBox.configure(text = "Wins: {}\nLosses: {}\nCurrent State: {}".format(
        countW, countT, currState))

def reset():
    global sides
    global countW
    global countT
    global currState
    sides.set(OPTIONS[0])
    countW = 0
    countT = 0
    currState = ""
    msgBox.configure(text = "msgBox")

#--Widgets--

text = Label(root, text = "Roll The Dice", bg = "lightgrey", font = customFont)

en = OptionMenu(root, sides, *OPTIONS)

btn = Button(root, text = "Roll The Dice", command = dice)

btn2 = Button(root, text = "Reset", command = reset)

msgBox = Label(root, text = "msgBox", bg = "lightgrey", font = ("ariel", 10))

#--Extra-Code--

text.grid(column = 1, sticky = N, padx = 250)

en.grid(column = 1, sticky = N, padx = 250)

btn.grid(column = 1, sticky = N, padx = 250)

btn2.grid(row = 0, rowspan = 1, column = 0, columnspan = 1, sticky = NW,
          padx = 10, pady = 10)

msgBox.grid(column = 1, sticky = N, padx = 250)

root.mainloop()
