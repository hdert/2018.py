'''
Author: Justin
Date: 13/6/2018
Version: V 0.1.1.6.5 Dev
'''

#--Librarys--

import random as rand

#--Variables--

name = ''
match = ''

#--Lists--



#--Dictionarys--



#--Classes--



#--Main-Code--

name = input(str('Enter Your Name: '))
victim = input(str('Enter Thier Name: '))

lovematch = int((len(name) * len(victim)) % 11)
print()
print('*' * lovematch)

if(lovematch >= 0 and lovematch <= 2):
    print('You Are A Terrible Match')

elif(lovematch >= 3 and lovematch <= 5):
    print('You Probably Shouldn\'t Bother')

elif(lovematch >= 6 and lovematch <= 8):
    print('You Are A Good Match')

else:
    print('You Are A Perfect Match')
    
