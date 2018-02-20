import sys

print("welcome to file read and write page")
fwrite = open('C:\cygwin64\home\y\workfile1.txt','w')

fread = open('C:\cygwin64\home\y\workfile1.txt','r')

print(fread.read())

for line in fread:
    print (line, end=' ')


fread.close()
fwrite.close()

print("end of python script")
