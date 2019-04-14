'''
Author: Justin
Date Started: 06/08/2018
Date Now: 08/08/2018
'''

# -- Librarys --

from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import random
from time import sleep as wait

# -- Setup --

root = Tk()
root.title("Battle")
root.geometry("700x700+10+10")

# -- Variables --

hp = 100
dff = 13

hpe = 100
dffe = 13

cTime = 60
setup = False

# -- Functions --

# - Main Functions -

def main():
    stWrite("You are attacked by an Orc",'')
    weapon()

def weapon():
    stWrite('\n[s]word, [a]xe, [h]ealing',
            '\nEnter your weapon choice: ')

def select(event = None):
    if setup == False:
        pass
    btn1.config(state = 'disabled')
    att = en.get()
    clear()
    if(att == ''):
        stWrite('\n\nYou entered nothing','')
    elif(att.lower() == 's'):
        stWrite('\n\nYou attack with your sword','')
        sword()
    elif(att.lower() == 'a'):
        stWrite('\n\nYou attack with your axe','')
        axe()
    elif(att.lower() == 'h'):
        stWrite('\n\nYou heal yourself','')
        heal()
    else:
        stWrite('\n\nNot a valid choice','')
    enemy_attack()

def enemy_attack():
    global hp, hpe, dff, dffe
    stWrite('\n\nThe Orc attacks you','')

    rand = random.randint(1, 20)
    if rand > dff:
        damage = random.randint(1, 20)
        stWrite('\nThe Orc Hits doing {} Damage\n'.format(
            damage),'')
        hp -= damage
    else:
        stWrite('\nThe Orc Misses\n','')
    btn1.config(state = 'normal')
    weapon()

# - Choices -

def sword():
    global hp, hpe, dff, dffe
    btn1.config(state = 'disabled')
    damage = 0
    rand = random.randint(1,20)
    if(rand > dffe):
        damage = random.randint(1,20)
        stWrite('\nyou hit with your sword doing {} damage'
                .format(str(damage)),'')
        hpe -= damage
    else:
        stWrite('\nyou miss with you sword','')

def axe():
    global hp, hpe, dff, dffe
    btn1.config(state = 'disabled')
    damage = 0
    rand = random.randint(1,20)
    if(rand > (dffe+2) ):
        damage = random.randint(5,30)
        stWrite('\nyou hit with your axe doing {} damage'
                .format(str(damage)),'')
        hpe -= damage
    else:
        stWrite('\nyou miss with you axe','')

def heal():
    global hp
    btn1.config(state = 'disabled')
    heal = random.randint(1,30)
    stWrite('\nYou heal yourself with {} hit points'
            .format(str(heal)),'')
    if( (hp + heal) > 100):
        hp = 100
    else:       
        hp += heal

# - Utilitys -

def clearSt():
    stWrite('','')
    
def clear():
    en.delete('0', END)

def stop(event = None):
    root.destroy()

def stWrite(text, text2):
    
    st.config(state = 'normal')
    if text != '':
        st.insert(END, text)
    else:
        st.delete('1.0', END)
    
    if text2 != '':
        st.insert(END, text2)

    st.yview(END)
    st.config(state = 'disabled')

# -- Frames --

f1 = Frame(root, width=300, height=200)

# -- Widgets --

st = ScrolledText(f1, state='disabled', bg='grey',
                  width=40, height=10, borderwidth = 3,
                  pady = 5)

en = ttk.Entry(f1)

btn1 = ttk.Button(f1, text="Enter", command=select)

btn2 = ttk.Button(root, text="Quit", command=stop)

btn3 = ttk.Button(root, text="Clear", command=clearSt)

# -- Code --

root.bind('<Return>', select)
root.bind('<Escape>', stop)

f1.place(x = 380, y = 10, anchor = N)

st.grid()

en.grid(pady = 10, padx = 5, ipadx = 50, sticky = W)
en.focus()

btn1.grid(column = 0, row = 1, sticky = E, ipadx = 5,
          padx = 20)

btn2.place(x = 5, y = 5)

btn3.place(x = 85, y = 5)

main()

root.mainloop()
