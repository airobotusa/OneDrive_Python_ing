string1 = "Python"
string2 = "Tutorial"

#Cancatenation
print(string1+string2)

#Repetition
print(string2 * 3)

#slicing
print(string2[3:6])

print(string2[:3])
print(string2[-3])  # 3rd from the last
print(string2[2:-3]) # 3rd to the 3rd from last. tor

#String type specific method: find(), replace(), split(), count()
print(string1.count('P', 0, 5))
print(string1.count('p', 0, 5))
print(string1.find('on'))




