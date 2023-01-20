# 16. WAP to determine the greatest number in between three user given number.

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

if num1 > num2 and num1 > num3:
    print(num1, " is greatest")
elif num2 > num1 and b > num3:
    print(num2, " is greatest")
else:
    print(num3, " is greatest")

# Output:
# Enter 1st number: 5
# Enter 2nd number: 8
# Enter 3rd number: 3
# 8  is greatest