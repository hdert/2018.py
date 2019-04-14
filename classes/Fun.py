'''
Author: Justin
Date: 11/6/2018
Version: V 0.1.2.2.1 Dev
'''

#--Librarys--

import random as rand

#-Lists-

weapons = ['sword', 'dagger', 'staff']

#-Dictionarys-

weapons_val = {'sword':[1, 15], 'dagger':[1, 6], 'staff':[1, 8]}

#--Variables--

user_input = ''
damage = ''

#--Main-Code--

user_input = input(str('''Pick a Weapon
sword, dagger or staff: '''))
damage = rand.randint(weapons_val[user_input][0], weapons_val[user_input][1])
print(damage)
