dict = {
  "Name" : "Amrendra",
  "Company" : "Hacker Kernerl",
  "Location" : "Arera Colony",
  "Age" : 22,
  "is_adult" : True,
  "subjects" : ["Python","C","Java"],
  "topics" : ("dict","set"),
  12 : 234,
  33.33 : 234,
  True : 234
}

print(type(dict))
print(dict)
print(dict['Name'])
print(dict['subjects'])

dict['Name'] = "Rahul"
dict['SurName'] = "Singh"
print(dict)


null_dict = {}
null_dict['SurName'] = "Singh"
print(null_dict)



student = {
    "name" : "Ram Singh",
    "subjects" : {
        "Hindi" : 12,
        "Chem" : 23,
        "Physics" : 23
    }
}

print(student)
print(student['subjects'])
print(student['subjects']['Chem'])