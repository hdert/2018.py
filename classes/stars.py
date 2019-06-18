num = (int(input('Put in a number: ')))
def hackerMan(amount):
    
    for i in range(1, amount+1):
        print('*' * i)


    for j in range(amount, 0, -1):
        print('*' * j)

hackerMan(num)
