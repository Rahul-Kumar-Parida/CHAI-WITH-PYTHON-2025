num=int(input("Enter a num: "))
check =True

if num<2:
    check=False
else: 
    for i in range(2,num):
        if(num%i==0):
            check=False
            break

if(check):
    print("Prime Number")
else:
    print("Not Prime Number")

