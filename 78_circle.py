#78. WAP that creates a dictionary of radius of a circle and its circumference
from math import pi

# r = {}
circle = {}
check = 1
while check == 1:
    r = int(input("Enter radius: "))
    check = int(input("Enter 1 to continue, -1 to exit: "))
    cir = round((2*pi*r),2)
    circle[r] = cir

print(circle)

# circle = {r: round((2*pi*r),2) for r in range(1,10)}
# print(circle)

'''
Output:
Enter radius: 5
Enter 1 to continue, -1 to exit: 1
Enter radius: 3
Enter 1 to continue, -1 to exit: 1
Enter radius: 7
Enter 1 to continue, -1 to exit: 1
Enter radius: 2
Enter 1 to continue, -1 to exit: 1
Enter radius: 4
Enter 1 to continue, -1 to exit: -1
{5: 31, 3: 19, 7: 44, 2: 13, 4: 25}
'''