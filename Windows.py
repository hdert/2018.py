prisonCell = ""
windows = int(input("Please enter the amount of windows in your home: "))

if windows < 0:
    print("\nI'm pretty sure thats impossible")
elif windows == 0:
    print("\nI'm beginning to suspect you live\nin some kind of military compound")
elif windows == 1:
    prisonCell = (str(input("\nDo you live in a prison cell?: ")))
elif(windows >= 30):
    print("\nYou must have one of\nthose new fangled\nglass houses")
else:
    print("\nYou have over one window\nyou must be doing well in life")

if prisonCell == 'yes' or prisonCell == 'Yes':
    print("\nOk")
elif prisonCell == 'maybe' or prisonCell == 'Maybe':
    print("Hmmmmm\n\nInteresting")
elif prisonCell == "":
    print()
else:
    print('\n"Sure"')
        
