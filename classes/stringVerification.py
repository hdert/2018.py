'''
Author: hdert
Date Started: 25/07/2018
Date Now: 25/07/2018
'''

# -- Librarys --

import random as rand

# -- Constant Lists --

animals = ['tiger', 'giraffe', 'elephant', 'hippo', 'wolf']

# -- Variables --

name = ""
passed = True

# -- Code --

while(True):
    name = input("Please Enter Your Name: ")
    passed = True
    
    try:
        if passed == True:
            int(name)
            passed = False
            print('''
Sorry That's Not A Valid Name
''')
            
    except:
        passed = True

    try:
        if passed == True:
            float(name)
            passed = False
            print('''
Sorry That's Not A Valid Name
''')
            
    except:
        passed = True
        
    if passed == True:
        break


