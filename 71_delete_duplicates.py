# 71. wap to remove all duplicate from a list.

a = [1, 1, 2, 3, 3, 4, 5, 6, 6]

print("Entire List: ", a)

a = list(set(a))

print("New list: ", a)


'''
Output: 
Entire List:  [1, 1, 2, 3, 3, 4, 5, 6, 6]
New list:  [1, 2, 3, 4, 5, 6]
'''