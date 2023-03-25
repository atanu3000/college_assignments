'''
54. WAP to calculate exponent of two number by using recursion.'''

def exp(b, p):
    if p == 0:
        return 1
    return b * exp(b, p-1)

a = int(input("Enter the base value: "))
b = int(input("Enter the power: "))

print(f'The ans is {exp(a, b)}')

'''
Output:
Enter the base value: 5
Enter the power: 4
The ans is 625
'''