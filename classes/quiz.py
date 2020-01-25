'''
Author: hdert
Date: 23/5/2018
'''

#--Librarys--

import random
import string

#--Variables--

guesses = 0
guess = 0
answer = ""
global score
score = 0

#--Functions--

def checkAnswer(a, b, c):
    if a == b:
        return("c")
    elif a == c:
        return("c")
    else:
        return("i")

#--Main-Code--

print('''
===========================================
====Welcome To The Quiz Of Millionare's====
===========================================
''')

answer = input(str("What is the nicest colour? "))
if checkAnswer(answer, "blue", "Blue") == "c":
    print("\nCorrect")
    score += 1
elif checkAnswer(answer, "blue", "Blue") == "i":
    print("\nIncorrect")
    
