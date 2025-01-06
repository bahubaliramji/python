tup  = (1,4,9,16,25,36,49,64,81,100,36)

x =  36

i = 0 #initialization
while i < len(tup):
    if(tup[i]==x):
        print("FOUND at idx",i)
        break
    else:
        print("finding..")
    i += 1

print("End of loop")
