# 18. WAP to take an input from user and check wheather it is number or character and determine it is uppercase or lowercase.

u_input = input("Enter an input: ")

if u_input >= 'A' and u_input <= 'Z':
    print("Uppercase")
elif u_input >= 'a' and u_input <= 'z':
    print("Lowercase")
elif u_input >= '0' and u_input <= '9':
    print("Number")
else:
    print("Special Char")

# Output:
# Enter an input: A
# Uppercase

# Enter an input: 5
# Number