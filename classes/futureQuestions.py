'''
Author: hdert
Date Started: 26/07/2018
Date Now: 26/07/2018
'''

# -- Librarys --

import random as rand

# -- Constant Lists --

answers = ['locations', 'yes', 'iron', 'reliability', 'vegetable', '7',
           'tadpole', 'camel']

questions = ['What\'s the difference between lava and magma?: ',
             'Can soap get dirty?: ',
             'Why do coins make your hands smell funny?: ',
             'What made the AK-47 so popular?: ',
             'Legally, are tomatoes fruits or vegetables?: ',
             'How many colors are there in a rainbow?: ',
             'What is a baby frog called?: ',
             'Which animal is known as the "Ship of the Desert"?: ']

# -- Variables --

rand_ = 0
answer = ''
answer = answers[0]
guess = ''
guesses = 0
points = 0

# -- Code --

while guesses < 10:

    rand_ = rand.randint(0, len(answers)-1)
    answer = answers[rand_]
    guess = input(questions[rand_])

    if answer == guess:
        print('\nCorrect\n')
        points += 1
    else:
        print('\nIncorrect\n')
        points -= 1
    guesses += 1
    
if points >= 8:
    print('You did really well, you got', int((points/10)*100), 'points')
elif points >= 5:
    print('You did okay, you got', int((points/10)*100), 'points')
else:
    print('You did not pass, you got', int((points/10)*100), 'points')
