with open("D:\python\lecture_7\demo_practice.txt","r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("D:\python\lecture_7\demo_practice.txt","w") as f:
    f.write(new_data)