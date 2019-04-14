n = 0
s = 0

while True:
    n = int(input())
    if n == 0:
        break
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (n * 3) + 1
        s += 1
    print(s)
    s = 0
        
