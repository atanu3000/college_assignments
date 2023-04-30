# 77. WAP that creates a dictionary of cubes of odd numbers in the range 1 to 10

odd_qubes = {x: x**3 for x in range(10) if x%2!=0}
print(odd_qubes)

'''
Output:
{1: 1, 3: 27, 5: 125, 7: 343, 9: 729}
'''