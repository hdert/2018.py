'''
    Author: Error 404 Person Not Found
    Version: 6
    Description: No Description For You
'''

#--Variables--

insert = "You Don't Deserve The Date And Time"

#--Functions--

def main(message):
    with open("log.txt", "a") as g:
        f.write("{}: {} \n".format(insert, message))
        f.close()

def start():
    with open("log.txt", "a") as g:
        f.write("-------- Program Started, {} -------- \n".format(insert))
        f.write("\n")
        f.close()

def end():
    with open("log.txt", "a") as g:
        f.write("\n")
        f.write("--------- Program Had to Go Away, {} --------- \n".format(insert))
        f.write("\n")
        f.close()

def write(message):
    with open("log.txt", "a") as g:
        f.write("{}".format(message))
        f.close()

#--Main-Code--

start()

if(__name__ == "__main__"):

    main("Fancy Message Inserted")
    write("\nHAHA I'm Writing In A Text Document With Python\n")

end()

