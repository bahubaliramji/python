str1 = "This is string"
str2 = 'This is string'
str3 = """This is string"""


# escape sequence character
# new line
str4 = "This is a string. \n we are creating it in the python"
print(str4)
# tab
str4 = "This is a string. \t we are creating it in the python"
print(str4)


# concatination
str1 = "Apna"
str2 = "ram"
str3 = str1+" "+str2
print(str3)

# length
print(len(str3))

# indexing
print(str3[3])
print(str3[1])
print(str3[4])
print(str3[7])

# manipulation is not available
# e.g. str3[3] = "g"

# slicing
print(str3[2:7])
print(str3[2:len(str3)])
print(str3[2:]) #[2:len(str)]
print(str3[:5]) #[0:5]

# negative index
print(str3[-3:-1])
