a1="Make a lot of money" 
a2="buy now"
a3="subscribe this"
a4="click this"

cmt=input("Enter cmt:")
if((a1 in cmt) or (a2 in cmt) or (a3 in cmt) or (a4 in cmt)):
    print("Spam Comment")
else:
    print("Good Comment")