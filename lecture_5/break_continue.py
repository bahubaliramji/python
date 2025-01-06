i = 1
while i <= 5:
    print(i)
    if(i==3):
        break
    i += 1

print("End of loop")


i = 1
while i <= 5:
    if(i==3):
        i += 1
        continue #skip
    print(i)
    i += 1

print("End of loop")


# odd
i = 1
while i <= 100:
    if(i%2==0):
        i += 1
        continue #skip
    print(i)
    i += 1

print("End of loop")