'''
Author: hdert
Date Started: 13/07/2018
Date Now: 13/07/2018
Version: V 0.1.1.5.5 Dev
'''

#--Librarys--

from tkinter import *

#--Set-Up--

root = Tk()
root.title("Graphical Window")
root.geometry("700x700+10+10")
root.configure(bg = "lightgrey")

#--Variables--

customFont = ("ariel", 14)
save = "lightgrey"
input2 = "lightgrey"
let = True

#--Functions--

def changeT(event = None):
    input_ = en.get()
    text.configure(text = input_)
    en.delete(0, END)
    
    
def changeC(event = None):
    global save
    global input2
    global let
    
    input2 = en.get()
    
    if input2 == "save":
        root.configure(bg = save)
        text.configure(bg = save)
        msgBox.configure(bg = save)
        msgBox.configure(text = "msgBox")
    else:
        try:
            root.configure(bg = input2)
            text.configure(bg = input2)
            msgBox.configure(bg = input2)
            msgBox.configure(text = "msgBox")
            let = True
        except:
            msgBox.configure(text = "Error:\nThat's Not A Colour")
            let = False
    en.delete(0, END)
    
    
def changeS(event = None):
    global input2
    global save
    
    if let == True:
        save = input2
        msgBox.configure(text = "msgBox")
    else:
        msgBox.configure(text = "Error, Not A Valid Colour")


def setS(event = None):
    global save

    root.configure(bg = save)
    text.configure(bg = save)
    msgBox.configure(bg = save)

#--Widgets--
        
text = Label(root, text = "The Devs Are Awesome", bg = "lightgrey", font = customFont)

en = Entry(root)

btn = Button(root, text = "Change Text", command = changeT)

btn2 = Button(root, text = "Change Colour", command = changeC)

btn3 = Button(root, text = "Save Current\nBackground Colour", command = changeS)

btn4 = Button(root, text = "Set Saved Background\nColour To Current", command = setS)

msgBox = Label(root, text = "msgBox", bg = "lightgrey", font = ("ariel", 10))

#--Extra-Code--

text.pack()

en.pack()
en.bind("<Return>", changeT)
en.focus()

btn.pack()

btn2.pack()

btn3.pack()

btn4.pack()

msgBox.pack()

root.mainloop()
