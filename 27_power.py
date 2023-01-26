# 27. WAP to calculate the power of a number.

base = int(input("Enter the base: "))
power = int(input("Enter the power: "))
res = 1
for i in range(power):
    res *= base

print("The result: ", res)

# Output:
# Enter the base: 5
# Enter the power: 4
# The result:  625