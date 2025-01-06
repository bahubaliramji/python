collection = {1,2,3,4,5,5,"Ram","King",6}

print(collection)
print(type(collection))
print(len(collection))

# empty_set 
collection2 = set()
print(type(collection2))

collection2.add(1)
collection2.add(3)
collection2.add(5)
collection2.add(5)
collection2.add(5)
collection2.add("hehehee")
print(collection2)

collection2.remove(5)
print(collection2)

collection2.add((1,2,3,4,44,4))
# collection2.add({1,2,3,4,44,4}) unhashable
print(collection2)

collection2.pop()
print(collection2)

collection2.pop()
print(collection2)

print(collection.union(collection2))
print(collection.intersection(collection2))

collection2.clear()
print(collection2)






