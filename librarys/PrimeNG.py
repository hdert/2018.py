#--Librarys--

import random

#--Variables--

Prime = []
num = 0
trys = 0
done = False

#--Functions--

def PrimeNGG(S, N):
    global done
    for n in range(S, N):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            Prime.append(n)
    done = True

def Start(s, x):
    global num
    global done
    if done == False:
        PrimeNGG(s, x)
    num = random.randint(s, x)

def Check():
    global Prime
    global trys
    for h in range(len(Prime)):
        if num == Prime[h]:
            print("Success")
            print("It Took You {} Trys".format(trys))
            return True
            break
                   
    print("Miss")
    trys += 1
    return False
