'''
Author: Jordan, hdert
Date: 26/06/2018
Version: V 0.1.1.4.2 Dev
'''

#--Definitions--

def terminate_user(name):
    return "Error 404 Person Not Found"

#--Variables--

hdert = "Error"
programmer = "hdert"

#--Main-Code--

if(hdert == "Error"):
    hdert = terminate_user("hdert")
    print("User Terminated")

if(programmer == "hdert"):
    program = "sucks"

print("{} your program {}".format(hdert, program))
