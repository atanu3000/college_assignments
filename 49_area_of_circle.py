'''
49. WAP to calculate the area of a circle using function.'''
from math import pi
def circle_area(rad):
    area = pi * rad ** 2
    return area

r = float(input("Enter the radius: "))

print(f'The area is {round(circle_area(r), 2)}')

'''
Output:
Enter the radius: 5
The area is 78.54
'''