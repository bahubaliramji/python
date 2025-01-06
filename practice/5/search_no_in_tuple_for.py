tup  = (1,4,9,16,25,36,49,64,81,100,36)

x =  49
idx = 0
for num in tup:
    if(num==x):
        print("FOUND at idx",idx)
        break    
    idx += 1

print("End of loop")
