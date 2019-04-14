import PrimeNG
z = int(input("Enter a number from 2 onwards: "))
b = int(input("Enter a number from {} onwards: ".format (z + 1)))
PrimeNG.Start(z, b)

while PrimeNG.Check() == False:
    PrimeNG.Start(z, b)

