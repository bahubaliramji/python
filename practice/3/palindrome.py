list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(list1 == copy_list1):
    print("palindrome")
else:
    print("Not palindrome")

copy_list2 = list2.copy()
copy_list2.reverse()

if(list2 == copy_list2):
    print("palindrome")
else:
    print("Not palindrome")