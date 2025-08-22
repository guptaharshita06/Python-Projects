#1. Write a program to print multiplication table of a given number using for loop.

n = input("Enter a number: ")
for i in range(1, 11):
    print(f"{n}X{i} = {n*i}")

#2. Write a program to greet all the person names stored in a list 'l' and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")
#3. Attempt problem 1 using while loop.

n = int(input("Enter a number: "))
i = 1
while(i<11):
    print(f"{n}X{i} = {n*i}")
    i += 1

#4. Write a program to find whether a given number is prime or not.

n = int(input("Enter a number: "))
for i in range(2,n):
    if(n%i) == 0:
        print("Number is not prime")
        break
else :
    print("Number is prime")

#5. Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter the number: "))
i = 0
sum = 0
while(i<=n):
    sum += i
    i += 1
print(sum)

#6. Write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter the number: "))
product = 1
for i in range(1, n+1):
    product = product*i

print(f"The factorial of {n} is {product}")

#7. Write a program to print the following star pattern.
#   *
#  ***
# ***** for n=3

n = int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "* (n-i), end = "")
    print("*"* (2*i-1), end = "")
    print("")

#8. Write a program to print the following star pattern.
# *
# **
# *** for n=3

n = int(input("Enter a number: "))
for i in range(1, n+1):
    print("*"* i, end="")
    print("")

#9. Write a program to print the following star pattern.
# ***
# * *
# *** for n=3

# Take input from user
n = int(input("Enter the number: "))

for i in range(1, n+1):
    if i == 1 or i == n:   # First or last row → print all stars
        print("*" * n)
    else:                  # Middle rows → stars at corners
        print("*" + " " * (n-2) + "*")


#10. Write a program to print multiplication table of n using for loops in reversed order.

n = int(input("Enter the number: "))
for i in range(1, 11):
    print(f"{n} X {11-i} = {n*(11-i)}")
