def decrement(n):
    return (lambda n: n - 1)(n)

num = int(input("Enter a number: "))

print(f'Ans is {decrement(num)}')

'''
Output:
Enter a number: 5
Ans is 4
'''