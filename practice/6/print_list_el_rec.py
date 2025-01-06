list = ["a","b","c","d","e","f","g"]
def print_el(list,index=0):
    if(index==len(list)):
        return
    print(list[index])
    print_el(list,index+1)


print_el(list)