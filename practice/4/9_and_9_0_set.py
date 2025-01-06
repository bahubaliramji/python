values = {9, 9.0, 9.23}
print(values)

values = {9, "9.0", 9.23}
print(values)

values = {int(9), float(9.0), 9.23}
print(values)

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)