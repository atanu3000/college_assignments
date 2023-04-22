# 66. wap that has a nested list to store toppers details. Edit the details and reprint the details.
info = [['Name:', 'Rohit'], ['Age:',25], ['Add:','Naihati']]

for i in info:
    print(i)

info[0][1] = 'Atanu'
info[1][1] = 19
print()

for i in info:
    print(i)


'''
Output:
['Name:', 'Rohit']
['Age:', 25]
['Add:', 'Naihati']

['Name:', 'Atanu']
['Age:', 19]
['Add:', 'Naihati']
'''