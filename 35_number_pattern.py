# 35. WAP to print a number pattern.

row = int(input("Enter the row: "))
count = 1

for i in range(1, row+1):
    for j in range(i):
        print(count, " ", end="")
        count += 1
    print()

'''
Output: 
Enter the row: 4

1
2  3
4  5  6
7  8  9  10
'''