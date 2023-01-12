# 8. WAP to calculate Simple Insterest where P, R, T are given by user.

p = int(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = int(input("Enter the time: "))

si = (p * r * t) / 100

print("Simple Interest: ", si)


# Output:
# Enter principal amount: 25000
# Enter rate of interest: 6.4
# Enter the time: 5
# Simple Interest:  8000.0