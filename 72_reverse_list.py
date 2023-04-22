# 72. wap to create a list of numbers in the specified range in perticular steps. reverse the list and print the values.

length = int(input("Enter the length of list: "))

list = [i for i in range(1, length + 1)]

# # Method 1
# list = list[::-1]

# Method 2
l = len(list)
for i in range(l // 2):
    list[i], list[l - 1 - i] = list[l - 1 - i], list[i]

# # Method 3
# l = len(list)
# for i in range(l // 2):
#     temp = list[i]
#     list[i] = list[l - 1 - i]
#     list[l - 1 - i] = temp

print(list)

'''
Output:
Enter the length of list: 10
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
'''