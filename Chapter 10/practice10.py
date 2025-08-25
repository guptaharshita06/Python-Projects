#1. Create a class "Programmer" for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Harry", 1200000, 245001)
print(p.name, p.salary, p.pin, p.company)
r = Programmer("Rohan", 1200000, 245001)
print(r.name, r.salary, r.pin, r.company)

#2. Write a class "calculator" capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")

a = Calculator(4)
a.square()
a.cube()
a.squareroot()

#3. Create a class with a class attribute a; create an object from it and set 'a' directly using object.a = o.Does this change the class attribute?

class Demo:
    a = 4
o = Demo()
print(o.a)  #Print the class attribute because instance attribute is not present
o.a = 0   #Instance attribute is set
print(o.a)  #Prints the instance attribute because instance attribute is present
print(Demo.a)

#4. Add a static method in problem 2, to greet the user wuth hello.

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is{self.n*self.n*self.n}")
    
    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")

    @staticmethod
    def hello():
        print("Hello, user!")

a = Calculator(4)
a.hello()
a.square()
a.cube()
a.squareroot()

#5. Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

from random import randint

class Train: 

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")

t = Train(12399)
t.book("Rampur", "Delhi")
t.book("Rampur", "Delhi")
t.book("Rampur", "Delhi")

#6. Can you change the self-parameter inside a class to something else(say "harry").Try changing self to "slf" or "harry" and see the effects.

