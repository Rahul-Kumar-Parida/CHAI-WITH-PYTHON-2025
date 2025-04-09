#1)
# lst=[2,3,4,5,6]
# print(max(lst))
# print(min(lst))

#2)
# lst2=[4,5,6,"rahul","kumar","Parida"]
# print(len(lst2))
# tup1=(1,2,3,4,"rr")
# print(len(tup1))
# str1="Rahul"
# print(len(str1))

#3)
# lst3=[3,4,5,6]
# print(sum(lst3))

#4)
# lst4=[4,6,2,9,5]
# print(sorted(lst4)) #asc
# print(sorted(lst4,reverse=True)) #desc

#5)
# n=-23.5
# print(abs(n))
# print(type(n))

#6)
# x=45.22332
# print(round(x,2))

#7)
# list1=[2,3,4]
# list2=['a','b','c','d']
# combine=list(zip(list1,list2))
# print(combine)

#8)
# num=[2,3,4,5,6]
# sq=list(map(lambda x:x**2, num))
# print(sq)

# def sq(x):
#     return x**2

# num=[1,2,3,4,5]
# sqq=list(map(sq,num))
# print(sqq)


num=[1,2,3,4,5,6]
odd=list(filter(lambda x:x%2!=0, num))
print(odd)

