a = int(input("Enter your age: "))

if(a%2 == 0):
    print("a is even")
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age")

else:
    print("You are not above the age of consent")

print("End of program")

#important notes
# There can be any number of elif statements.
# Last else is executed only if all the conditions inside elifs fail.
