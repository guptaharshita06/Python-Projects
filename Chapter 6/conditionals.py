a = int(input("Enter your age: "))
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("Age cannot be negative")

elif(a==0):
    print("Age cannot be zero")
    
else:
    print("You are below the age of consent")

print("End of program")
