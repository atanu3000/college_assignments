# 37. WAP to print a number pattern.

row = int(input("Enter the row: "))

for i in range(1, row+1):
    for j in range(1, row+1-i):
        print("  ", end="")     # "2 spaces"
    for j in range(1, i+1):
        print(j,"", end="")     # "1 space"
    for j in range(i-1, 0, -1):
        print(j,"", end="")     # "1 space"
    print()

'''
Output:
Enter the row: 4
      1 
    1 2 1 
  1 2 3 2 1 
1 2 3 4 3 2 1 
'''