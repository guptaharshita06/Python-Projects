#Write a program to store 7 fruits in a list entered by a user.

fruits = []
f1 = input("Enter fruit name: ")
fruits.append(f1)
f2 = input("Enter fruit name: ")
fruits.append(f2)
f3 = input("Enter fruit name: ")
fruits.append(f3)
f4 = input("Enter fruit name: ")
fruits.append(f4)
f5 = input("Enter fruit name: ")
fruits.append(f5)
f6 = input("Enter fruit name: ")
fruits.append(f6)
f7 = input("Enter fruit name: ")
fruits.append(f7)
print(fruits)

#Write a program to accept marks of 6 students and display them in a sorted manner.

marks = [23,18,9,28,25]
marks.sort()
print(marks)

#Check that a tuple type cannot be changed in Python.
#Write a program to sum a list with 4 numbers.

l = [35,23,6,3]
print(sum(l))

#Write a program to count the number of zeroes in the following tuple.
a = (7,0,8,0,0,9)
n = a.count(0)
print(n)
