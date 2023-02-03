# 33. WAP to print number pattern.

row = int(input("Enter the row: "))

for i in range(1, row+1):
    for j in range(i):
        print(i, " ", end="")
    print()

'''
Output:
Enter the row: 5

1
2  2
3  3  3
4  4  4  4
5  5  5  5  5
'''