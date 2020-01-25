'''
Author: hdert
Date Started: 31/07/2018
Date Now: 31/07/2018
'''

# -- Librarys --

import random as rand

# -- Constant Lists --

teachers = ['Mr Wright',
            'Mr Bennett',
            'Mr Johnson',
            'Mrs Johns',
            'Dr Graham',
            'Mr Gibbs']

students = ['Sione',
            'Ivan',
            'Lenny',
            'Jasprit',
            'Bailey',
            'Lucas',
            'hdert',
            'Brodie']

# -- Variables --

choice = ''
teacher = rand.choice(teachers)
hpt = 100
student = rand.choice(students)
hps = 100
rand_ = 0
damage = 0

# -- Code --

while(hpt > 0 and hps > 0):
    print('You\'re on duty and you\'re attacked')

    choice = input('''
[b]ionic, [s]hout
Choose you're attack: ''')
    
    if choice == 'b':
        print('\nYou use your bionic abilitys\n')

        rand_ = rand.randint(1, 20)
        
        if rand_ > 13:
            damage = rand.randint(1, 20)
            hps -= damage
            print('Your attack worked doing, {} Damage\n'.format(damage))
        else:
            print('Your bionic attack failed\n')
        
    elif choice == 's':
        print('\nYou use your words\n')
        
        rand_ = rand.randint(1, 15)
        
        if rand_ > 13:
            damage = rand.randint(1, 15)
            hps -= damage
            print('Your attack worked doing, {} Damage\n'.format(damage))
        else:
            print('Your verbal attack failed\n')

    print('You\'re walking along and are attacked')
    
    choice = input('''
[p]rofanity, [s]cream
Choose your attack: ''')
    
    if choice == 'p':
        print('\n******! *****! ***!\n')

        rand_ = rand.randint(1, 15)
        
        if rand_ > 13:
            damage = rand.randint(1, 15)
            hpt -= damage
            print('Your attack worked doing, {} Damage\n'.format(damage))
        else:
            print('Your immaturity failed\n')
        
    elif choice == 's':
        print('\nAHHHHHHHHHHH!\n')
        
        rand_ = rand.randint(1, 20)
        
        if rand_ > 13:
            damage = rand.randint(1, 20)
            hpt -= damage
            print('Your attack worked doing, {} Damage\n'.format(damage))
        else:
            print('Your immaturity failed\n')
    print('''
Student Hitpoints: {}
Teacher Hitpoints: {}
'''.format(hps, hpt))

if hpt > 0 :
    print('{} has survived {}\'s viciousness'.format(teacher, student))

else:
    print('{} has pinned {}'.format(student, teacher))
