# 16. WAP to determine the greatest number in between three user given number.

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a > b and a > c:
    print(a, " is greatest")
elif b > a and b > c:
    print(b, " is greatest")
else:
    print(c, " is greatest")

# Output:
# Enter 1st number: 5
# Enter 2nd number: 8
# Enter 3rd number: 3
# 8  is greatest