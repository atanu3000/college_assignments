'''
53. WAP to determine the GCD of two numbers by using recursion.'''

def gcd(a, b):
    if a%b == 0:
        return b
    return gcd(b, a%b)

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

print(f'The GCD of {a} and {b} is {gcd(a,b)}')

'''
Output:
Enter 1st number: 16
Enter 2nd number: 24
The GCD of 16 and 24 is 8
'''