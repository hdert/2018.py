'''
Author: hdert
Date Started: 04/07/2018
Date Now: 04/07/2018
Version: V 0.1.1.1.1 Dev
'''

#--Librarys--

from tkinter import *
import random as rand

#--Setup--

root = Tk()
root.title("Graphics")
root.geometry("700x700+10+10")

#--Lists--

colours = ["lightgrey", "grey", "blue", "red"]

#--Variables--

color = "lightgrey"
customFont = ("ariel", 14)
points = 0

#--Definitions--

def addPoints():
    global points
    points += 1
    point.configure(text = str(points))
    point.pack

def bgChange():
    global colours
    color = rand.choice(colours)
    point.configure(bg = color)
    root.configure(bg = color)
    point.pack()

#--Widgets--

point = Label(root, text = "0", font = customFont, bg = color)
point.pack()
add = Button(root, text = "Add Points", command = addPoints)
add.pack()
btn = Button(root, text = "Change The Colour", command = bgChange)
btn.pack()

#--Extra-Code--

root.configure(bg = color)

root.mainloop()
