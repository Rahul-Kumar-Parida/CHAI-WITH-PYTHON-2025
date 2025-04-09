class Employee:
    language="Python" #this is class attribute
    salary=120000

    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print("I am Creating an object")

    def getinfo(self):
        print(f"The Language is {self.language}. The salary is {self.salary} ")
    @staticmethod
    def greet():
        print("Good Morning")
    
harry=Employee("Rahul",3400,"c++")
print(harry.language,harry.salary)


