# 5. WAP to calculate area and perimeter of circle

radius = int(input("Enter the radius: "))
pi = 3.14159

area = round((pi * radius * radius), 2)
peri = round((2 * pi * radius), 2)

print("Area of circle is: ", area)
print("Perimeter of circle is : ", peri)


# Output:
# Enter the radius: 5
# Area of circle is:  78.54
# Perimeter of circle is :  31.42