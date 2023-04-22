# 74. wap to caculate distance between two points.

x = (int(input("Enter x1: ")), int(input("Enter y1: ")))
y = (int(input("Enter x2: ")), int(input("Enter y2: ")))

dis = ((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2) ** 0.5

print(f"Distance between {x} and {y} is : {round(dis, 2)}")

'''
Output:
Enter x1: 3
Enter y1: 2
Enter x2: 5
Enter y2: 6
Distance between (3, 2) and (5, 6) is : 4.47
'''