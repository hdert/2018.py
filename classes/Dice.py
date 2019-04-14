'''
Author: Justin
Date: 13/4/2018
Program: calling a method
'''

#--Librarys--

import random

#--Variables--

printy = 0
roll = 0

#--Main-Code--

def D20():
    return random.randint(1, 20)

print("I'm going to get a random number\n\n")

while True:
    printy = D20()

    if roll >= 100:
        break

    if printy == 8 or printy == 11:
        print("You rolled an", printy, "\n")
    else:
        print("You rolled a", printy, "\n")

    roll += 1
    
    if(printy == 20):
        print("Yay you rolled a twenty\n\n")
        print("You rolled", roll, "times")
        break
