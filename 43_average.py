'''
43. WAP to return average of passing arguments using function.'''

def avg(*a):
    sum = 0
    for i in a:
        sum += i
    return sum / len(a)

average = avg(5, 3, 7, 8)
print(f'The average is: {average}')

'''
Output:
The average is: 5.75
'''