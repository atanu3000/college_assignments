# 58. WAP to use lamnda function as a argument of an ordinary function.

def large(a, b):
    if a > b:
        return a
    return b

sum = lambda x, y: x + y
sub = lambda x, y: x - y

print(f'Large of two number: {large(sum(10, 5), sub(10, 5))}')

'''
Output: 
Large of two number: 15
'''