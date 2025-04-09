#1)
# num=-9
# if num>0:
#     print("Positive")
# elif num==0:
#     print("Zero")
# else:
#     print("Negetive")


#2)
# for i in range(1,11):
#     print(i,end=' ')

#3)
# num=5
# i=1
# while i<=10:
#     print(f"{num} *  {i} =  {num*i}")
#     i+=1

# #4)
# def fact(num):
#     if(num==1 or num==0):
#         return 1 
#     return num*fact(num-1)
# print(fact(5))

#5)
# num=1
# if num<2:
#     print("Not Prime")
# else:
#     for i in range(2,int(num**0.5)+1):
#         if(num%i==0):
#             print("Not Prime")
#             break
#     else:
#         print("Prime")


#6)
# num=5
# a=0
# b=1
# c=0
# if(num==0):
#     print(0)
# elif num==1:
#     print(1)
# else:  
#     for i in range(2,num+1):
#         c=a+b
#         a=b
#         b=c
#     print(c)

# # 7)
# num1=2
# num2=6
# num3=4
# if(num1>=num2 and num1>=num3):
#     print(num1)
# elif(num2>=num1 and num2>=num3):
#     print(num2)
# elif(num3>=num1 and num3>=num2):
#     print(num3)

# #8)
# for i in range(1,101):
#     if(i%2==0):
#         print(i)

# 9)
# str1="Rahul"
# n=len(str1)-1
# while n>=0:
#     print(str1[n],end='')
#     n=n-1

# print(str1[::-1])

# 10)
str1="racecar"
rev=str1[::-1]
if str1==rev:
    print("Palindrome")
else:
    print("Not Palindrome")