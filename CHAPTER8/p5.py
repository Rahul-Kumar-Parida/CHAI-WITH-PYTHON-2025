# n=3
# while(n>0):
#     print(" * " * n)
#     n=n-1


def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)
pattern(3)