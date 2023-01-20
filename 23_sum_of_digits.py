# 23. WAP to calculate the sum of the digits of a number.

num = int(input("Enter a number: "))

sum = 0

while num > 0:
    rem = num % 10
    sum += rem
    num //= 10

print("Sum of the digits: ", sum)

# Output:
# Enter a number: 369
# Sum of the digits:  18