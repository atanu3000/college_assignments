'''
45. WAP to calculate two number is equal or not using function.'''

def isEqual(num1, num2):
    if num1 == num2:
        return "Equal"
    return "Not equal"

a = int(input("Enter first number: "))
b = int(input("Enter second number:"))

print("The numbers are: ", isEqual(a, b))

'''
Output:
Enter first number: 4
Enter second number:6
The numbers are:  Not equal
'''
