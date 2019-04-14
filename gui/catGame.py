'''
Author: Justin
Date Started: 13/08/2018
Date Now: 16/08/2018
'''

# -- Librarys --

from tkinter import *

# -- Setup --

root = Tk()
root.title("Ball Game")
root.geometry("700x700+10+10")

# -- Variables --

image_ = 0
img1 = PhotoImage(file = "cat1.gif")
img2 = PhotoImage(file = "cat2.gif")
x = 350
y = 350

# -- Constant Lists --

IMAGE_LIST = [img1, img2]

# -- Functions --

def change(event):
    global x, y, IMAGE_LIST, img1, img2, image_

    if event.char == 'w':
        image = 0
        canvas.delete("all")
        y -= 10
        canvas.create_image(x, y, image = IMAGE_LIST[image_], tags = 'cat')
        canvas.move("cat", x, y)
        
    elif event.char == 'a':
        if image_ == 0:
            image_ = 1
        else:
            image_ = 0
        canvas.delete("all")
        x -= 10
        canvas.create_image(x, y, image = IMAGE_LIST[image_], tags = 'cat')
        canvas.move("cat", x, y)

    elif event.char == 's':
        image = 0
        canvas.delete("all")
        y += 10
        canvas.create_image(x, y, image = IMAGE_LIST[image_], tags = 'cat')
        canvas.move("cat", x, y)
        
    elif event.char == 'd':
        if image_ == 0:
                image_ = 1
        else:
            image_ = 0
        canvas.delete("all")
        x += 10
        canvas.create_image(x, y, image = IMAGE_LIST[image_], tags = 'cat')
        canvas.move("cat", x, y)

def remove(event = None):
    root.destroy()
    
# -- Widgets --

canvas = Canvas(root, bg = "white", width = 700, height = 700)

# -- Code --

root.bind("<w>", change)
root.bind("<a>", change)
root.bind("<s>", change)
root.bind("<d>", change)
root.bind("<Escape>", remove)

canvas.pack(anchor = NW)
canvas.create_image(x, y, image = IMAGE_LIST[image_], tags = 'cat')

root.mainloop()
