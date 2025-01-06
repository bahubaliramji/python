# immutable

tuple = (2,13,3,4,556,6,6,45)
print(tuple)
print(tuple[0])
print(tuple[2])
# tuple[1] = 1

tup = ()
print(tup)
print(type(tup))

tup = (1)
print(tup)
print(type(tup))

tup = (1,)
print(tup)
print(type(tup))

# slicing
print(tuple[1:4])


print(tuple.index(6))
print(tuple.count(6))