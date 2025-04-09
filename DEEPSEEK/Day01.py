# #datatypes and variable in python
# name="rahul"
# age=24
# height=5.7
# placed=False

# #now i want to check the data types of each
# print(type(name))  #class str
# print(type(age))   #class int
# print(type(height)) #class float
# print(type(placed))  #class bool

# #now i want input something
# name=input("Enter your name: ")
# age=int(input("Enter Your Age: "))
# height=float(input("Enter Your Height: "))
# gender=input("Enter Your Gender: ")

# print(f"my name is {name} and i am {age} years old and my height is {height} and gender {gender}")


#now i want to learn operators like arithmatic, comparision, and logical operator
#1)arithmatic
# print(10+5)
# print(10-5)
# print(10*5)
# print(10/5)
# print(10%5)
# print(10**2)

#2)comparision operator
# print(5>4)
# print(5<4)
# print(5==4)
# print(5==5)
# print(5!=4)
# print(5!=5)
# print(6>=6)
# print(6<=6)

#3)logical operator
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# print(not True)
# print(not False)


#now i want conditional statements
age=int(input("Enter your age: "))
if age>18:
    print("You are eligible")
elif age>15 and age<18:
    print("You are not eligible ")
else:
    print("You are still child")


#practice problem

check= int(input("Check number is even odd:"))
if(check%2==0):
    print("Even")
else:
    print("Odd")
