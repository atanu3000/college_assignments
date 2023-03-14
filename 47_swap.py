'''
47. WAP to swap two number using number.'''

def swap(a, b):
    a, b = b, a
    print(f'After swapping: a = {a}, b = {b}')

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

print(f'Before swapping: a = {a}, b = {b}')
swap(a, b)

'''
Output:
Enter 1st number: 10
Enter 2nd number: 20
Before swapping: a = 10, b = 20
After swapping: a = 20, b = 10
'''
