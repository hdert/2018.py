'''
'''

#--Librarys--

import random as randm
import string

#--Variables--

name = ''
adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange', 'yellow',
              'green', 'blue', 'purple', 'fluffy', 'white', 'proud', 'brave']
nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon', 'hammer', 'duck',
         'panda']

#--Main-Code--

name = input(str("Enter Your Name: "))

print("Hello", name, "welcome to Password Picker\n")

adjective = randm.choice(adjectives)

noun = randm.choice(nouns)

number = randm.randrange(0, 100)

special_char = randm.choice(string.punctuation)

password = adjective + noun + str(number) + special_char + "@gmail.com"

print("Your super secure password is %s" % password)
