# function definition
def calc_sum(a,b): #parametere
    return a+b

sum = calc_sum(10,20) #function call; arguments
print(sum)

def print_hello():
    print("Hello")


print_hello()
print(print_hello())


def cal_prod(a,b=3): #default parameter
    print(a*b)
    return a*b


cal_prod(23)