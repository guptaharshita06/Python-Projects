class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"This language is {self.language}. The salary is {self.salary}")

    def greet():
        print("Good morning")

harry = Employee()
#harry.language = "JavaScript" # This is an instance attribute
harry.greet()
harry.getInfo()
#Employee.getInfo(harry)
# print(harry.language, harry.salary)
