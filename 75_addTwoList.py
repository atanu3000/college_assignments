#75. WAP that combaines the two list to a dictonary;

keys = ['Name', 'roll', 'address']
values = ['Ram', '01', 'kolkata']
details = zip(keys, values)
data = dict(details)
print(data)

'''
Output:
{'Name': 'Ram', 'roll': '01', 'address': 'kolkata'}
'''