student = {
    "name" : "Ram Singh",
    "subjects" : {
        "Hindi" : 12,
        "Chem" : 23,
        "Physics" : 23
    }
}

print(student)

print(list(student.keys()))

print(len(student))
# print(len(list(student.keys())))

print(student.values())

# print(list(student.items()))
pairs = list(student.items())
print(pairs[0])

print(student.get("name"))
print(student["name"]) #can show error
print(student.get("Surname"))

student.update({"city":"bhopal", "age":23, "name": "Amrendra"})
print(student) #can show error

