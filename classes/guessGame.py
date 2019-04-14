'''
Author: Justin
Date Started: 06/07/2018
Date Now: 06/07/2018
'''

#--Librarys--

import random as rand

#--Constant-Variables--

rand_ = rand.randint(1, 100)

#--Variables--

error = False
trip = False
guess = 0
guesses = 0

#--Main-Code--

name = input("Enter Your Name: ")

while True:

    while True:
        trip = False
        try:
            guess = int(input("\nEnter A Number: "))
            error = False
        except:
            print('''
Whoops That Isn't A Valid Number Try
Putting In A Number Between 1 And 100
''')
            guesses += 1
            error = True
            trip = True
        if guess <= 0 and trip == False:
            print('''
Whoops That Isn't A Valid Number Try
Putting In A Number Between 1 And 100
''')
            guesses += 1
            error = True
        elif guess > 100 and trip == False:
            print('''
Whoops That Isn't A Valid Number Try
Putting In A Number Between 1 And 100
''')
            guesses += 1
            error = True
        if error == False:
            break
    if guess == rand_:
        print('''
You Guessed Right It Took You {} Trys
'''.format(guesses))
        print('''Thanks For Playing {}'''.format(name))
        break
    elif guess > rand_:
        print('''
You Guessed To High
''')
        guesses += 1
    elif guess < rand_:
        print('''
You Guessed To Low
''')
        guesses += 1
    
