"""
# p1 - Write a Python program to print "Hello Python".
print("Hello Python")
"""

"""
#p2 -Write a Python program to do arithmetical operations addition and division.

num1=float(input("Enter Num1: "))
num2=float(input("Enter Num2: "))
res=num1+num2
print(f"The Sum is: {res}")

num3=float(input("Enter Num3: "))
num4=float(input("Enter Num4: "))
if num4==0:
    print("Error: Division is not allowed by Zero!")
else:
    div_res=num3/num4
    print(f"Division : {div_res}")
"""

"""
# p3 - Write a Python program to find the area of a triangle
base=float(input("Enter Base: "))
Height=float(input("Enter Height: "))
area=0.5*base*Height
print(f"The Area Of triangle: {area}")
"""
"""
# p4 - Write a Python program to swap two variables.
v1=input("Enter variable 1:")
v2=input("Enter variable 2:")
# v1,v2=v2,v1
temp=v1
v1=v2
v2=temp
print(f"Var1:{v1}  and Var2:{v2}")
"""

"""
# p5- Write a Python program to generate a random number.
import random
print(f"Random Number: {random.randint(1,100)}")
"""

"""
#p6- Write a Python program to convert kilometers to miles.
km=float(input("Enter distance in KM: "))
# 1km =0.621371 miles
conv_factor=0.621371
miles=km*conv_factor
print(f"{km} kilometers is equal to {miles} miles")

"""
"""
#p7- Write a Python program to convert Celsius to Fahrenheit.
celcius=float(input("Enter temperature in celsius: "))
fahrenhit=(celcius*9/5)+32
print(f"{celcius} degrees Celsius is equal to {fahrenhit} degrees fahrenhit.")
"""

""" 
#p8 write a Python Program to display calender
import calendar
year=int(input("Enter Year: "))
month=int(input("Enter month: "))
cal= calendar.month(year,month)
print(cal)

"""

"""
#p9 write a Python Program To solve Quadratic Equation.
import math
a=float(input("Enter Coefficient a: "))
b=float(input("Enter Coefficient b: "))
c=float(input("Enter Coefficient c: "))

dis= b**2-4*a*c

if dis>0:
    root1=(-b+math.sqrt(dis)) / (2*a)
    root2=(-b-math.sqrt(dis)) /(2*a)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif dis==0:
    root = -b/(2*a)
    print(f"Root : {root}")
else:
    real_part=-b/(2*a)
    imaginary_part = math.sqrt(abs(dis))/(2*a)
    print(f"Root 1: {real_part} + {imaginary_part} i")
    print(f"Root 2: {real_part} - {imaginary_part} i")

    
"""
""""""
#p10- Write a Python program to swap two variables without temp variable.
a=5
b=6
print(f"Before Swapping: a:{a},  b:{b}")
a,b=b,a
print(f"After Swapping: a:{a},  b:{b}")