# with open("D:\python\lecture_7\practice.txt","r") as f:
#     data = f.read()
#     print(data)
#     num  = ""
#     for i in range(len(data)):
#         if(data[i] == ","):
#             print(int(num))
#             num = ""
#         else:
#             num += data[i]



count = 0
with open("D:\python\lecture_7\practice.txt","r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    print(nums)

    for val in nums:
        if(int(val)%2==0):
            count += 1

print(count)

