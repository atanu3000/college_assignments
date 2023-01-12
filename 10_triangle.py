# 10. WAP to calculate area of a irregular triangle.

a = int(input("Enter the 1st side: "))
b = int(input("Enter the 2nd side: "))
c = int(input("Enter the 3rd side: "))

s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print("The the area of the triangle: ", round(area, 2))

# Output:
# Enter the 1st side: 5
# Enter the 2nd side: 6
# Enter the 3rd side: 7
# The the area of the triangle:  14.7