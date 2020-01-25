'''
Author: hdert
Date: 20/6/18
Version: V 0.1.1.1.1 Dev
'''

#--Librarys--

import random as rand

#--Lists--

names = ['Bob', 'Sam', 'Fred', 'Carl', 'George', 'Jill', 'Betty']

#--Variables--

name = 'Sam'

#--Main-Code

print('Before Encryption', name)
a = (chr(ord('s')+len(name)))
b = (chr(ord('a')+len(name)))
c = (chr(ord('m')+len(name)))
name = a+b+c
print('After Encryption', name)
