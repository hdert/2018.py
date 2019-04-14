'''
Name: Guessing
Date: 11/4/2018
Author: Justin
Version: Dev Build/V.0.1 "Aligator"
'''
#--Librarys--

import random

#--Variables--

random = random.randint(1, 100)
guess = 0
counter = 0

#--Main-code--

print('''
==========================================
Welcome to my guessing game guess a number
between 1 and 100 and see if your guess
was correct.
==========================================
''')

#This code was a "guess" :) as to how this would work
'''while True:
    guess = int(input("Put your guess here: "))
    if guess >= 101:
        print("invalid number")
                
    elif guess <= 0:
        print("invalid number")
                
    elif guess == random:
        print("Yay! You guessed it")
'''
while True:
    guess = int(input("Put a number between 1 and 100 here: "))
    counter += 1
    if guess == random:
        print("\nYou got it correct!")
        break
    
    elif guess > random:
        print("Go lower\n")
        
    elif guess < random:
        print("Go higher\n")
        
    elif guess <= 0:
        print("invalid numer\n")

    elif guess >= 101:
        print("invalid number\n")

print("\n\nIt took you {} guesses to get the number".format (counter))
