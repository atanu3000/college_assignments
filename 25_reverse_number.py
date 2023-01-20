# 25. WAP to reverse of a given number.

num = int(input("Enter a number: "))

num1 = 0

while num > 0:
    rem = num % 10
    num1 = num1 * 10 + rem
    num //= 10

print("Reverse of the number: ", num1)

# Output:
# Enter a number: 852
# Reverse of the number:  258