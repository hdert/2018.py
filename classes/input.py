job = ""
answer = ""
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
print("\n", name, "\n", age)

if(name == "Justin" or name == "justin"):
    print(" Hey that's me")
elif(name == "francis" or name == "Francis"):
    print(" Like my name Francis?")
elif(age > 18):
    job = (str(input("Do you have a job?: ")))

if(job == ""):
    print()
else:
    print("Ok")     
    answer = (str(input("Would you like an echo of your answer?: ")))

if(answer == "yes" or answer == "Yes"):
    print('"', job, '"')
    
