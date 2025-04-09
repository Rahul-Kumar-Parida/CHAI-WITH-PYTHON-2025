st="Hey harry you are amazing"
f=open("file.txt",'a')
f.write(st)
f.close()

f=open("file.txt")
data=f.read()
print(data)
f.close()