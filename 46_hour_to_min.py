'''
46. WAP to convert time into minutes using function.'''

def min(hr, min):
    return hr * 60 + min

h = int(input("Enter the hour: "))
m = int(input("Enter the min: "))

print(f'The converted min: {min(h, m)}')

'''
Output:
Enter the hour: 5
Enter the min: 12
The converted min: 312
'''