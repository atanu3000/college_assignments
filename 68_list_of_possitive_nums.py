#wap that  have a list of number possitive and negetive. Make a new tupple that only has possitive value from this list.

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
