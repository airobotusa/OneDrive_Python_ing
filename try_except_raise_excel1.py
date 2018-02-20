import sys

print("This is try:   except practice in chapter 7\n")

print("To open file at C:/Users/y/AppData/Local/Programs/Python/Python36-32/myfile.txt\n")

# comment line
# C:/Users/y/AppData/Local/Programs/Python/Python36-32/myfile1.xlsx

try:
#   f = open('myfile.txt')
    
    fread = open('C:/Users/y/AppData/Local/Programs/Python/Python36-32/myfile.txt')
    #print("Before for loop\n")
    count =0
    for line in fread:
        #s = fread.readline()
        #s=line.readline()
        #i = int(s.strip())
        #i = line
        #print("Before converting int(line.strip()")
        count +=1
        i = int(line.strip())
        print(count,"th Result of i is :", i)
    
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

    fread.close()
