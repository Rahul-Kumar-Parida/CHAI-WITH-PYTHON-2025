"""
#1) Basic Function Syntax
#Write a Function To Calculate and return the square of a number

def square_of_num(num): #parameter
    return num**2
print(square_of_num(8))
"""

"""
#2)Functions With Multiple Parameters
#Create a function that takes two numbers as parameters and return their sum.

def sum(a,b):
    return a+b
print(sum(2,3))
"""

"""
#3)Polymorphism in Python
#write a function, that multiplies two numbers, but can also accept and multiply string
def multiply(a,b):
    return a*b
print(multiply(4,5))
print(multiply("Rahul",5))
print(multiply(4,"Rahul"))
"""

"""
#4)Function Returning Multiple Values
#Create a function that returns both the area and circumference of a circle given its radius.

def multiple_values(radius):
    area=3.14*radius*radius
    cricum=2*3.14*radius
    return area,cricum

a , c = multiple_values(4)
print("area", round(a,2), "Circumference: ",round(c,2))
"""

"""
#5) Default Parameter Value
#write a function that greets a user. If no Name Is Provided it should greet with a default name.

def greet(name="Rahul"):
    return f"Good Morning , {name}"

print(greet("Rohit"))
"""
"""
#6)Lambda Functions
#Create a Lambda Function to compute the cube of a number.
cube=lambda x:x**3
print(cube(3)) #27
cube(3) #27
"""

"""
#7)Function With *args
def sum_all(*args):
    print(*args) #input
    print(args) #tuple(input)
    return sum(args)

print(sum_all(3,4,5,6))

"""

"""
#8) Function With  **kwargs
def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(power="Lazer" ,name="Rahul")
print_kwargs(power="Lazer" ,name="Rahul", level="Zero")
print_kwargs(name="Sab")

"""
"""
#9) Generator Function With Yield
#Write a Generator Function that yields even numbers up to a specified limit

def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i
    
for num in even_generator(10):
    print(num)
"""
"""
#10) Recursive Function

def factorial(num):
    if num==0:
        return 1
    return num* factorial(num-1)

print(factorial(5))
"""


