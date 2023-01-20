# 20. WAP to calculate the root of a quadratic equation.

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

d = b**2 - (4*a*c)
root1 = (-b + d**0.5) / 2*a
root2 = (-b - d**0.5) / 2*a

if d > 0:
    print("Different roots.")
    print(root1)
    print(root2)
elif d == 0:
    print("Same roots")
    print(root1)
    print(root2)
else:
    print("Imaginary roots")
    print(root1)
    print(root2)

# Output:
# Enter value of a: 1
# Enter value of b: 5
# Enter value of c: 6
# Different roots.
# -2.0
# -3.0

# Enter value of a: 2
# Enter value of b: 6
# Enter value of c: 9
# Imaginary roots
# (-6+6j)
# (-6-6j)