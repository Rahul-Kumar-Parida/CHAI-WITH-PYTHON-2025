#Lable the program written in problem 4 with comments,

import os #import


#specify the directory you want to list
directory_path="/"

#list all files and directories
contents=os.listdir(directory_path)

#print each file and directory name
for item in contents:
    print(item)

print(contents)