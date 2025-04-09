class Employee:
    language="Python" #this is class attribute
    Salary=120000

harry=Employee()
harry.name="Harry" #this is an object attribute/instance
print(harry.name,harry.Salary,harry.language)

rohan=Employee()
rohan.name="Rohan"
print(rohan.name,rohan.Salary,rohan.language)
#Here name is object attribute and salary and language are class attributes as they directly belong to the class,