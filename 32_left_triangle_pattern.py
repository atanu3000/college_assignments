# 32. WAP to print a left triangle pattern.

row = int(input("Enter the row: "))

for i in range(1, row+1):
    for j in range(i):
        print("* ", end = "")
    print()

'''
Output:
Enter the row: 5

* 
* * 
* * * 
* * * * 
* * * * * 
'''