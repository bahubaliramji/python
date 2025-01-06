num1 = int(input("Neter the first no: "))
num2 = int(input("Neter the second no: "))
num3 = int(input("Neter the third no: "))
# if(num1>num2 and num1>num3):
if(num1>num2):
    if(num1>num3):
        print("Greatest no. is first:",num1)
elif(num2>num3):
    print("Greatest no. is second:",num2)
else:
    print("Greatest no. is third:",num3)

