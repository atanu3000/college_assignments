# 69. wap using filter function to a list of squares of numbers from one to ten. then use the for... in construct to sum the element in the list generated.

def square(x):
    if x >= 1 and x <= 10:
        x = x ** 2
        return True

# print(list)

add = filter(square, range(1, 11))
sum = 0

for i in add:
    sum += i ** 2

print(sum)

'''
Output: 
385
'''
