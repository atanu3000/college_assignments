# 67. wap that accepts different number of arguments and return sum only the possitive values passed to it.

a = []
n = int(input("Enter the no. of nums: "))
print("Enter the values: ")
for i in range(n):
    a.append(int(input()))

sum = 0
for i in a:
    if i > 0:
        sum += i

print('Sum = ', sum)

'''
Output: 
Enter the no. of nums: 5
Enter the values:
3
2
4
-6
2
Sum =  11
'''