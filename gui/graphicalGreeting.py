'''
Author: Justin
Date: 27/6/18
Version: V 0.1.1.4.3 Dev
'''

#--Librarys--

from tkinter import *

#--Objects--

root = Tk()
root.title("JAGW")
root.geometry("800x700+250+20")

#--Definitions--

def change():
    but.configure(text = "Thank You")

#--Variables--

sv = StringVar()

#--Main-Code--

name = Label(root, text = "Name:", font = "ariel")
name.pack()
food = Entry(root, textvariable = sv, font = "ariel")
food.pack()
your_name = Label(root, textvariable = sv, font = "ariel")
your_name.pack()
but = Button(root, text = "Verify That You Have Read The T's & C's"
             , command = change())
but.pack()

root.mainloop()
