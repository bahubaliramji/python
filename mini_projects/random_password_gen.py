import random
import string

# random.choice([1,2,4,5,6,7,8,9,0])

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

charValues = string.ascii_letters+string.digits+string.punctuation

# print(random.choice(charValues))

password_len = int(input("Enter length of passowrd: "))

password = ""
for i in range(password_len):
    password += random.choice(charValues)

print(password)


# list comprehension
res = "".join([random.choice(charValues) for i in range(password_len)])
# res = "*".join([random.choice(charValues) for i in range(password_len)])
print(res)


