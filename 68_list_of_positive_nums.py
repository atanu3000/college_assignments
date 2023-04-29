#wap that  have a list of number positive and negetive. Make a new tuple that only has positive value from this list.

a = []
n = int(input("Enter the no. of nums: "))
print("Enter the values: ")
for i in range(n):
    a.append(int(input()))

print('Entire elements: ', a)

b = ()
for i in a:
    if i >= 0:
        b += (i,)

print('Possitive elements: ', b)

'''
Output:
Enter the no. of nums: 5
Enter the values:
3
-5
2
-4
6
Entire elements:  [3, -5, 2, -4, 6]
Possitive elements:  (3, 2, 6)
'''