'''
Author: hdert
Version: Dev V.0.1
Program-Goal: Hangman
Date: 13/4/2018
'''
#--Librarys--

import random

#--Variables--

#Hey you
words = ["apple", "android", "bixby", "walkman", "shopping", "darude", "spaggeti"]
#Don't look at this
word = words[random.randint(0, 6)]
man = ''

#--Main-Code--

letter = str(input("Enter a letter: "))

for i in range(len(word)):
    if letter == word[i]:
        print(word[i])
    else:
        print("_")

print("_ " * len(word))
