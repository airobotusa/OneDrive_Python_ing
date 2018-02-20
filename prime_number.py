print("10 hours Video link:< https://youtu.be/Vxw1b8f_yts >")
print("\n***<Python Tutorial for Beginners . From the basics to advanced topics> on YouTube *** \n")
print("Prime number only")

#num = input("enter upto what number:")

num = 30
print("num is : ", num)
num2 = int(num)
for i in range(2,num2):
	j =2
	counter =0
	while j < i:
		if i % j ==0:
			counter = 1
			j = j +1
		else:
			j = j +1
	if counter ==0:
		print(str(i) + " is a prime number")
	else:
		counter =0

print("end of program")
print("while counter")

#str =  input("Start anykey for next while loop")

counter1 = 0
while counter1 < 50:
	if counter1 ==10:
		break
	else:
		pass
	print(counter1)
	counter1 += 1

for i in "Python":
	if i == "h":
		continue
	print(i)

for i in range(0,5):
	if i < 2:
		continue
	print(i)

print("\n try and except")
try:
	if name > 3:
		print("Hi")
except:
	print("Python ran into an error. Pls check code")
	print("Python ran into an error. Pls check code22")
	
print("** Control statement : Break, Continue and Pass(BCP) **\n")
for i in range(0,5):
	if i < 2:
		continue
	print(i)
	
print("** #Comment **")
#> compares the first objectto the second object
# if is a conditional statement
"""
ajfdlfj
alfjd
"""
print("** Quick tips**")
string = "adkfjksdjfsdjf"
print(string)
string = "It's a nice day!"
print(string)
string = 'It\'s a nice day!'
print(string)

blue2 = "OK"

if blue2 \
==\
"cheese":
	if blue2 == "OK":
		print("OK")
	else:
		print("NO GOOD")
else:
	print("No else")
	
print("** Function**")
for i in range(0,5):
	print("HI")
i=0
def Hi5():
	if i in range(0,5):
		print("i value is :", i, "HI")
	else:
		print("***")
def multiply(num1, num2):
	total = num1 * num2
	return total
	
print("Calling Hi5()")

Hi5()

print("** Calling multiply()")
print("multiply(20, 24) is ", multiply(20, 24))

print("** Abs and Bool ** Built in function **")

print("abs(-43 is : ", abs(-43))
print("bool(None) is ", bool(None))

print("** Now Help and Dir **")
print("dir([\"add\"]) is ", dir(["add"]))
tiger = "I am a tiger"
print("\n***dir(tiger) is :", dir(tiger))
print("\n** help(tiger.upper) is :" , ( help(tiger.upper)))

print("** eval(\"print(\'Hello\'))\" is:" ,eval("print('hello')"))
eval("print('hello')")

program = '''
print('Hi there')
print('My name is Bob')
'''
exec(program)

print("*** int, float, str() **")
#age = input("Enter your age: ")
age = 34
print(age)
print(int(age))
print(str(age))
print("*** Summary **")

print("len([23, 34,254,22]) is : ", len([23, 34,254,22]))
print("len(\"AABBCC\") is : ", len("AABBCC"))
array1=['a','b','c']
print("array1=['a','b','c'] , max is :",  max(array1))
array2=['a','b','c',"A", "D"]
print("array2=['a','b','c',\"A\", \"D\"] min is :",min(array1))

list1 = [ 12,213,24,255,455]
print(sum(list1))

print("*** Basic of Classes ***")
class ClassName:
	pass
instance = ClassName()
class Students:
	def __init__(self, name, age, grade):
		self.name=name
		self.age=age
		self.grade= grade
student1 = Students("Bob", 12, "7th")
print("student1.name is :", student1.name)
print("student1.age is : " , student1.age)
print("student1.grade is : ", student1.grade)

print("*** Functions in classes ***")
class Students:
	def __init__(self, name, age):
		self.name=name
		self.age=age
	def displayStudent(self):
		return("Student name is " + self.name + "and age is " + str(self.age))
Stu = Students("Chad", 15)
print("Stu.displayStudent() is ", Stu.displayStudent())
#2:38:24
class Parent:
			def func(self):
				print("This is a parent function")
class Child(Parent):
	def func(self):
		print("This is a child function")

c =Child()
print("Calling c.func()")
c.func()  # printing This is a Child function. because overriding method.
print("** File IO **")
file1 =  open("myfile.txt", "r")
print("file1.read()\n", file1.read())
print("file1.tell() is: \n", file1.tell())


