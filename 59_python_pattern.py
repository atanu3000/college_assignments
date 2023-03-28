'''
59. print the pattern:  p 
                        p y 
                        p y t 
                        p y t h 
                        p y t h o
                        p y t h o n
'''

ch = 'python'

for i in range(len(ch)):
    for j in range(i+1):
        print(ch[j],"",end="")
    print()

'''
Output:
p 
p y 
p y t 
p y t h 
p y t h o
p y t h o n
'''