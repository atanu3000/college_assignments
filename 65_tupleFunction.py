# 65 wap using a function that return the circumfarrence and area of a circle who's radius is passed as an arguments.

def circle(r):
    area = 3.14 * r * r
    circum = 2 * 3.14 *r
    return (area, circum)

radius = int(input("Enter the radius: "))


(area, circum) = circle(radius)

print("Area of the circle is: ", area)
print("Circumference of the circle is: ", circum)

'''
Output: 
Enter the radius: 5
Area of the circle is:  78.5
Circumference of the circle is:  31.4
'''