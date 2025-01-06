f = open("D:\python\lecture_7\demo.txt","r+") # no truncate pointer at starting
f.write("\n abc")
print(f.read())
f.close()


f = open("D:\python\lecture_7\demo.txt","w+") # truncate and pointer at starting
print(f.read())
f.write("\n abc")
f.close()

f = open("D:\python\lecture_7\demo.txt","a+") # no truncate and pointer at end
print(f.read())
f.write("\n abc")
print(f.read())
f.close()