#--Librarys--

from random import randint as rand

#--Main-Code--

a = int(input("Pick a number: "))
b = int(input("Pick another number over {}: ".format(a+1)))

print("Here's a random number between {} and {}: {}".format(a, b, rand(a+1, b-1)))
