'''
Author: hdert
Date Started: 07/08/2018
Date Now: 07/08/2018
'''

# -- Librarys --

import random as rand

# -- Constant Lists --

NAMES = ['Darrel',
         'Aaron',
         'Samantha']

# -- Variables --

choice = 0
name = ''
rand_ = 0

# -- Functions --

def batt():
    global choice
    choice = choice.lower()
    print('''
You chose {} and your opponent chose {}
'''.format(,choiceO()))

def choiceO():
    global rand_
    rand_ = rand.randint(1, 3)
    if rand_ == 1:
        return 'Rock'
    elif rand_ == 2:
        return 'Paper'
    elif rand_ == 3:
        return 'Scissors'
         

# -- Code --

while True:
    name = input('Please enter your name: ')
    choice = input('''[R]ock
[P]aper
[S]cissors
Please choose a move: ''')

    try:
        if choice.lower() == 'r' or choice.lower() == 'p' or choice.lower() == 's':
            batt()
        else:
            print('''
Sorry that's an invalid move
''')
    except:
        print('''
Sorry that's an invalid move
''')
