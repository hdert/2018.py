'''
Author: hdert
Date Started: 02/07/2018
Date Current: 02/07/2018
Version: V 0.1.1.1.3 Dev
'''

#--Librarys--

from tkinter import *

#--Object-Setup--

root = Tk()
root.title("Graphics in Future Proof")
root.geometry("800x700+250+20")

#--Variables--

text_ = StringVar()

#--Definitions--

def color():
    colour = text_.get()
    try:
        root.config(bg = colour)
        greeting.config(bg = colour)
    except:
        pass
    
def name():
    name = text_.get()
    greeting.configure(text = name)
    greeting.pack


#--Main-Code--

root.config(bg = "lightgrey")
greeting = Label(root, text = "Name", bg = "lightgrey", fg = "black", font = ("ariel", 18))
greeting.pack()
en = Entry(root, textvariable = text_)
en.pack()
btn = Button(root, text = "Name", command = name)
btn.pack()
wrote = Button(root, text = "colour", command = color)
wrote.pack()
root.mainloop()
