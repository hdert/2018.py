'''
Author: hdert
Date: 12/6/2018
Version: V 0.1.1.6.2 Dev
'''

#--Librarys--

import random as rand
import string as strg

#--Definitions--

def name_seq():
    return input(str("Enter Your Name: "))

#--Variables--

_secret_ = 'Bob Bobson'
_c_ = 0

#--Dictionarys--



#--Lists--

_wrong_ = ['\nWhat, Thats Nowhere Close To My Name\nTry Again', '\nReally?\nTry Again',
           '\nMy First Name Is _ _ _ The Builder\nTry Again', '\nMy Last Name Is My First Name Plus My Son']

#--Main-Code--

print("\nHello", name_seq())
while (True):
    _b_ = input(str('\nGuess My Name: '))

    if _b_ == _secret_:
        print('\nWell Done You Guessed Right After {} Trys'.format(_c_))
        break
    else:
        print(rand.choice(_wrong_))
        _c_ += 1
