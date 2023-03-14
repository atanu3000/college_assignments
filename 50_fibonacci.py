'''
50. WAP to print the fibonacci series using functin upto a given range.'''

def fib(len):
    a, b = 0, 1
    for i in range(1, len+1):
        print(f'{a} ', end="")
        c = a + b
        a, b = b, c

l = int(input("Enter the range: "))

fib(l)

'''
Output:
Enter the range: 6
0 1 1 2 3 5
'''