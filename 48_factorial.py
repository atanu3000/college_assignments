'''
48. WAP to calculate factorial of a given number using function.'''

def factorial(num):
    fact = 1
    for i in range(2, num+1):
        fact *= i
    return fact

n = int(input("Enter a number: "))

print(f'The factorial of {n} is: {factorial(n)}')

'''
Output:
Enter a number: 6
The factorial of 6 is: 720
'''