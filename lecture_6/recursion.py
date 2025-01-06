def show(n):
    print(n)
    if(n==1): #base case
        return
        # pass
        
    show(n-1)

show(5)



def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

print(factorial(4))