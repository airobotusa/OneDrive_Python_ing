print("file_open2")

#fwrite = open('C://Users/y/python/ws_users.xlsx','a')
#fread = open('C://Users/y/python/users.txt','r')
fwrite = open('C://Users/y/python/sample_sql.sql','a')
fread = open('C://Users/y/python/users1.txt','r')
fread2 = open('C://Users/y/python/sample_sql.sql','r')

for line in fread:
    line = line.split("\t")
    print("I am here and executing fwrite.write ")
    fwrite.write("insert into wp_users ( ID, user_login, user_name ) values (%s, '%s', '%s')\n" % (line[0], line[1], line[2]))
    print("fread.read() executing")
    print("fread is executing: ==1>\n" ,fread.read())
    print("fread2 executing: ==2>", fread2.read())
    
fread.close()
fwrite.close()

print("End of it")
