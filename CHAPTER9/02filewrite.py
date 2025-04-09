st="Hey RAHUL you are amazing"
f=open("file.txt",'w')
f.write(st)
f.close()

f=open("file.txt")
data=f.read()
print(data)
f.close()