# 21. WAP to calculate the factorial of a number given by user.

num = int(input("Enter a number: "))

fact = 1

for n in range(1, num+1):
    fact *= n

print(f"Factorial of {num} is = {fact}")

# Output:
# Enter a number: 5
# Factorial of 5 is = 120