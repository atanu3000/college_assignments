'''
52. WAP to print fibonacci series upto a given range by using recursion.'''

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

t = int(input("Enter no. of term: "))

for i in range(t):
    print(f'{fib(i)} ', end="")


'''
Output:
Enter no. of term: 6
0 1 1 2 3 5
'''