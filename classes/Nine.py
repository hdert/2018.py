'''
Author: hdert
Date: 15/6/2018
Version: V 0.1.1.4.4 Dev
'''

#--Librarys--

import random as _rand
import string as _str

#--Variables--

rand = _rand.randint(1, 100)
letter = _str.punctuation
name = ''

#--Main-Code--

name = input(str("Enter A Name: "))

if name in "Bob Sam Carl Joe Betty".split():
    print("\n" + name)
else:
    print("\nYour Name Is Not\nOn The Guest List")
