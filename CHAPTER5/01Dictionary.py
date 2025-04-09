marks={
    "Harry":100,
    "Shubham":56,
    "Rohan":23
}
print(marks,type(marks))
print(marks["Harry"])

# dictionaries method
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Harry":99})
print(marks)

print(marks.get("Harry"))
print(marks["Harry"])

# print(marks.get("Harry2")) #none
# print(marks["Harry2"]) #return error
d={}
print(type(d))