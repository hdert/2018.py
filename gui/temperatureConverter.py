'''
Author: Justin
Date Started: 04/07/2018
Date Now: 04/04/2018
Version: V 0.1.1.4.3 Dev
'''

#--Librarys--

from tkinter import *

#--Tk-Setup--

root = Tk()
root.title("Temperature")
root.geometry("700x700+10+10")

#--Variables--

colour_ = "lightgrey"
customFont = ("ariel", 24, "italic", "bold")

#--Definitions--

def convertF():
    f = en.get()
    celsius = ((float(f) - 32)* 5 / 9)
    text_.configure(text = str(celsius))

def convertC():
    c = en.get()
    farenheit = ((float(c) * 9 / 5) + 32)
    text_.configure(text = str(farenheit))

#--Widgets--

en = Entry(root)
en.pack()
text_ = Label(root, text = "Calculation Goes Here", font = customFont, bg = colour_)
text_.pack()
text2 = Label(root, text = "Temperature Converter", font = "ariel", bg = colour_)
text2.pack()
btn = Button(root, text = "Farenheit To Celsius", command = convertF, relief = RAISED, bg = colour_)
btn.pack()
btn2 = Button(root, text = "Celsius To Farenheit", command = convertC, relief = RAISED, bg = colour_)
btn2.pack()

#--Main-Code--

root.configure(bg = colour_)

root.mainloop()
