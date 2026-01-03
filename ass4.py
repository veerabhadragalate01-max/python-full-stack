
# Get password input from user
password = input("Enter a password: ")

#Checks (each returns True or False)
length_check = len(password) >= 8
upper_check = any(char.isupper() for char in password)
lower_check = any(char.islower() for char in password)
digit_check = any(char.isdigit() for char in password)
print(length_check)
print(upper_check)
print(lower_check)
# print(digit_check)

# length_check = len(password) >= 8
# upper_check = any(char.isupper() for char in password)
# lower_check = any(char.islower() for char in password)
# digit_check = any(char.isdigit() for char in password)