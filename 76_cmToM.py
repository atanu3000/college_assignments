#76. write a program that creates two dict. one that stores convertion values from m to cm and another one stores convertion values from cm to m.

m_cm = {x: x *100 for x in range(1,11)}
#print(m_cm)
temp = m_cm.values()
#print(temp)
cm_m = {x: x /100 for x in temp}

print("Mtrs to Cms: ", m_cm)
print()
print("Cms to Mtrs: ", cm_m)


'''
Output:
Mtrs to Cms:  {1: 100, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600, 7: 700, 8: 800, 9: 900, 10: 1000}

Cms to Mtrs:  {100: 1.0, 200: 2.0, 300: 3.0, 400: 4.0, 500: 5.0, 600: 6.0, 700: 7.0, 800: 8.0, 900: 9.0, 1000: 10.0}
'''