#questions on conditionals
#1) Age group categorization
"""
Classify a Person's age group : Child(<13),Teenager(13-19), Adult (20-59), Senior (60+).

person_age=int(input("Enter Your age: "))

if person_age<13 and person_age>0:
    print("You are a Child!")
elif person_age>=13 and person_age<=19:
    print("You are a Teenager!")
elif person_age>=20 and person_age<=59:
    print("You are an Adult!")
elif person_age >=60:
    print("You are a Senior")
else:
    print("Invalid age ")

"""
#2)Movie Ticket Pricing
"""
Movie Tickets are Priced based on age: $12 for adults(18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
"""
age =30
day ="wednesday"
price= 12 if age>=18 else 8

if day=="wednesday":
    price-=2

print(price)