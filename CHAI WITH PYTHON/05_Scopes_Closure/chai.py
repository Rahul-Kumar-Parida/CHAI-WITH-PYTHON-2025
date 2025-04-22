x=99
# def func2(y):
#     z=x+y
#     return z

# result=func2(1)
# print(result)


#avoid global keyword

# def f1():
#     x=88
#     def f2():
#         print(x)
#     f2()
# f1() #88


def f1():
    x=88
    def f2():
        print(x)
    return f2
myResult = f1()     #closure
myResult()
