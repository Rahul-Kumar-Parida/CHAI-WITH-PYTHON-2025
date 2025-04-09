class Programmer:
    company="Microsoft"
    salary=120000
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin 

p=Programmer("Harry",1200033,453456)
r=Programmer("rahul",1300033,123456)
print(p.name,p.salary,p.pin,p.company)
print(r.name,r.salary,r.pin,r.company)

