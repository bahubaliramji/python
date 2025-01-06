cities = ["delhi", "gurgaon", "noida", "pune", "mumbai"]
heroes = ["Thor", "Bahubali", "hANUMAN", "dad"]

def print_len(list):
    print(len(list))

print_len(heroes)
print_len(cities)

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(cities)
print()
print_list(heroes)