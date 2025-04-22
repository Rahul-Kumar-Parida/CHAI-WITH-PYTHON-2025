"""
#1) Counting positive Numbers.

numbers = [10, -5, 20, -15, 30, -25, 40, -35]

pos_count=0
for i in numbers:
    if i>0:
        pos_count+=1
print(f"Positive Numbers: {pos_count}")

# pos_num=[i for i in numbers if i>0]
# print(pos_num)
"""

"""
#2)Sum Of Even numbers upto n given.
n=10
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum+=i
print(f"Sum of Even Numbers upto {n} is: {sum}")
"""

"""
#3)Multiplication table printer
num=4
for i in range(1,11):
    if i==5:
        continue
    print(f"{num} X {i} = {num*i}")

"""
"""
#4) Reverse a String using loop
name="God is Not Supporting me"
for i in range(len(name)):
    print(name[len(name)-1-i],end="")

    """
"""
#5) Find the First Non-Repeated Characters.
input_str="teeterl"
for char in input_str:
    if input_str.count(char)==1:
        print(char)
        break
"""
"""
#Factorial Calculator

num=5
i=1
fact=1
while i<=num:
    fact*=i
    i+=1
print(fact)
"""

"""
#7 Validate Input
while True:
    num=int(input("Enter a Number: "))
    if num>0 and num<=10:
        print("Thanks")
        break
    else:
        print("Invalid Number, try Again!!")
"""
"""
#8) Prime Number Checker!!
num=88
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("Not a Prime Number!!")
            break
    else:
        print("Prime Number")
else:
    print("Not a Prime Number!!")

    """

"""

#9)unique items
items=["apple","banana","orange","apple","mango"]
unique_item=set()
for item in items:
    if item in unique_item:
        print("Duplicate Item, ",item)
        break
    unique_item.add(item)

"""
"""
#10 Exponential backoff
import time
wait_time=1
max_retries=5
attempts=0
while attempts<max_retries:
    print("Attempt ", attempts+1, "wait time: ", wait_time+1)
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1

    """


    