fo = open("foo.txt", "r+")
textentry = input("type here: ")
fo.write(textentry)
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
str = fo.read(10)
print ("Read String is : ", str)
fo.close()
