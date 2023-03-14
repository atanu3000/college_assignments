'''
44. WAP to calculate even or odd number using function.'''

def even_odd(num):
    if num % 2 == 0:
        return "Even"
    return "Odd"

n = int(input("Enter a number: "))
print("The number is: ", even_odd(n))

'''
Output:
Enter a number: 5
The number is:  Odd
'''