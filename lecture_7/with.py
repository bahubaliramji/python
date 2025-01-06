with open("D:\python\lecture_7\demo.txt","r") as f:
    # no need to close file with automatically do it
    data = f.read()
    print(data)


with open("D:\python\lecture_7\demo.txt","w") as f:
    # no need to close file with automatically do it
    f.write("new data")
    # print(data)