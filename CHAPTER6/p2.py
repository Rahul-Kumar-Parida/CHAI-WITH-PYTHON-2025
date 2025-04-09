m1=int(input("Enter 1:"))
m2=int(input("Enter 2:"))
m3=int(input("Enter 3:"))
percent = ((m1+m2+m3)/300)*100

if(m1>=33 and m2>=33 and m3>=33 and percent>=40):
    print("Pass",percent)
else:
    print("Fail",percent)