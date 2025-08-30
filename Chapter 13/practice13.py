#1. Create two virtual enviornments, install few packages in the first one. How do you create a similar enviornment in the second one?



#2. Write a program to input name, marks and phone number of a student and format it using the format function like below:
# The name of the student is Harry, his marks are 72 and phone number is 99999888

name = input("Enter name: ")
marks = int(input("Enter marks: "))
phone = int(input("Phone number: "))

s = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone)
print(s)

#3. A list contains the multiplication table of 7. Write a program to convert it to vertical string of same numbers.

table = [str(7*i) for i in range (1,11)]
s = "\n".format(table)
print(s)

#4. Write a program to filter a list of numbers which are divisible by 5.

def divisible5(n):
    if(n%5 == 0):
        return True
    return False
a = [1,2,34234,53,6234235, 64343, 65, 754, 45,55]

f = list(filter(divisible5, a))
print(f)

#5. Write a program to find the maximim of the numbers in a list using the reduce function.

from functools import reduce
a = [111,2,65,53,635,65,74,45,55]
def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater, 1))

#6. Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.

# pip freeze > requirements.txt
# virtualenv harryenv

#7. Explore the 'Flask' module and create a web server using Flask & Python.

