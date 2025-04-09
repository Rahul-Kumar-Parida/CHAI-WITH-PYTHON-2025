class Employee:
    language="Python" #this is class attribute
    salary=120000

    def getinfo(self):
        print(f"The Language is {self.language}. The salary is {self.salary} ")
    @staticmethod
    def greet():
        print("Good Morning")
    
harry=Employee()
harry.getinfo()
Employee.getinfo(harry)
harry.greet()

