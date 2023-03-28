# 63. WAP to reverse a string 
str = "Hello"

#print(str[::-1])

rev = ''

for i in range(len(str)-1, -1, -1):
    rev += str[i]

print("Reverse string is: ", rev)

'''
Output:
Reverse string is:  olleH
'''