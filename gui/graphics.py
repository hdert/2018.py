'''
Author: hdert
Date: 29.06.2018
Version: V 0.1.1.1.1 Dev
'''

#--Librarys--

from tkinter import *

#--Objects--

root = Tk()
root.title("JAGW")
root.geometry("800x700+250+20")

#--Variables--

fontstyle = ("ariel", 15)

#--Main-Code--

label1 = Label(root, bg = "grey", fg = "black", padx = 30, pady = 10, text = "Show me", font = fontstyle)
label1.pack()

root.mainloop()
