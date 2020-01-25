'''

Author: hdert
Version: Dev V.1.0
Date: 16,5,2018

'''

#--Librarys--

import random as randm

#--Functions--

def enRace():
    return race[randm.randint(0, 2)] #--Enemy-Oponents--

#--Variables--

name = ""
hp = 100 #--Hit-Points--
dff = 30 #--Defense--
dmg = 0 #--Damage--
race = ['Human', 'Orc', 'Wolfen'] #--Oponents--
enHp = 100 #--Ennemy-Hit-Points--
enDff = 13 #--Enemy-Defense--
enDmg = 0 #--Enemy-Damage--
att = 0 #--Attack-Type--
rand = 0 #--Random-Attack-Value--
damage = 0 #--Damage-Given--

#--Main-Code--

name = input(str("Enter Your Name: "))

while(True):
    print("You are attacked")
    att = input("Hit with sword[s]")
    rand = randm.randint(1, 20)

    if (rand > enDff):
        print("You hit your enemy\n")
        damage = randm.randint(10, 30)
        enHp -= damage
    else:
        print("You miss\n")
