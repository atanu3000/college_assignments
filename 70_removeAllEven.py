# 70. wap to create a number of list in the range from 1 to 10 then delete all the even num from the list and print the final list.

list = [i for i in range(1, 11)]

print("Entire list: ", list)

for i in list:
    if i % 2 == 0:
        list.pop(list.index(i))

print("New list: ", list)

'''
Output:
Entire list:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
New list:  [1, 3, 5, 7, 9]
'''