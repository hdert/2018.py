'''

Author: hdert
Date: 25/5/2018
Desc: Input Validation
Version: Dev Build V.0.1.6.9.1

'''

#--Librarys--



#--Definitions--



#--Variables--

choice = ""
number = 0

#-Main-Code--

while(choice != "e"):
    '''
    while(True):
        choice = input("Enter a, b, or c: ")
        if(choice.lower() == 'a' or choice.lower() == 'b' or choice.lower() == 'c'):
            break
    '''
    if(number >= 1 and number <= 100):
        break
    
    while(True):
        try:
            number = int(input("Enter a number between 1 and 100: "))
        except:
            print("You did not enter a valid number")

        if(number >= 1 and number <= 100):
            break
        else:
            print("The Number has to be between 1 and 100")
