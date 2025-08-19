# Write a program to create a dictionary of hindi words with values as their English translation. Provide user with an option to look it up.

words = {
    "madad": "Help",
    "Kursi": "Chair",
    "billi": "Cat"
}

word = input("Enter the word you want meaning of: ")
print(words[word])

# Write a program to input eight numbers from the user and display all the unique numbers(once).

s = set()
n = input("Enter number 1: ")
s.add(int(n))
n = input("Enter number 1: ")
s.add(int(n))
n = input("Enter number 1: ")
s.add(int(n))
n = input("Enter number 1: ")
s.add(int(n))
n = input("Enter number 1: ")
s.add(int(n))
n = input("Enter number 1: ")
s.add(int(n))
n = input("Enter number 1: ")
s.add(int(n))
n = input("Enter number 1: ")
s.add(int(n))

print(s)

# Can we have a set with 18(int) and '18'(str) as a value in it.

s = set()
s.add(18)
s.add("18")
print(s)

# What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') #Length of a s after these operations?
print(len(s))


# s = {} What is the type of s.
# ans = dictionary
s = {}
print(type(s))

#Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

d = {}
name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang}
         )
name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})
print(d)

# If the names of 2 friends are same; What will happen to the program in problem 6?
# ans = The values entered later will be updated.

# If languages of two friends are same; what will happen to the program in problem 6?
#Nothing will happen. The value will be same.

# Can you change the values inside  a list which is contained in set s?
s = {8,7,12,"Harry", {1,2}}
