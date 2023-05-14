# 79. WAP that creates two sets, one of the number from 1 to 10 and other has all the prime numbers in the range.

set1 = set()
set2 = set()

set1 = {x for x in range(1, 11)}

def prime(num):
    flag = True

    if num == 1 :
        flag = False

    for i in range(2, num):
        if (num % i) == 0:
            flag = False
            break
    return flag
    

set2 = {x for x in set1 if prime(x)}

print(set1)
print(set2)


'''
Output:
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
{2, 3, 5, 7}
'''