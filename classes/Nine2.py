'''
Author: hdert
Date: 15/6/2018
Version: V 0.1.1.1.1 Dev
'''

#--Librarys--

import random as rand
import string as _str

#--Lists--

words = ['pizza', 'fries', 'yogurt', 'otter', 'plane']

#--Variables--

lives = 9
secret_word = rand.choice(words)
clue = list('?' * len(secret_word))

#--Main-Code--

