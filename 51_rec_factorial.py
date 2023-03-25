'''
51. WAP to calculate factorial of a number by using recursion.'''

def facto(n):
    if n == 0 or n == 1:
        return 1
    return n * facto(n-1)

n = int(input("Enter a number: "))
print(f"Factotial of {n} is {facto(n)}")

'''
Output: 
Enter a number: 6
Factotial of 6 is 720
'''