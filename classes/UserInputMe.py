'''

Author: hdert
Date: 25/5/2018
Desc: Input Validation
Version: Dev Build V.0.1.8.3

'''

#--Librarys--



#--Definitions--

def check():
    a = input(str("Enter a, b or c: "))
    return a
    if a == "a" or a == "b" or a == "c":
        print("Valid Input")
    elif a == "A" or a == "B" or a == "C":
        print("Invalid Input")
        print("Try using lowercase letters\n")
        check()
    else:
        print("Invalid Input")
        check()


#--Variables--

choice = ""

#-Main-Code--

choice = check()
