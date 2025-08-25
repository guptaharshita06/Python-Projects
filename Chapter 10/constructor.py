class Employee:
    language = "Python"  # This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language):  # Dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"This language is {self.language}. This salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

harry = Employee("Harry", 1300000, "JavaScript")
# harry.name = "Harry"
print(harry.name, harry.salary)

rohan = Employee()
