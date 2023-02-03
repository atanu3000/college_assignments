'''
38. WAP to calculate the sum of following series:
    1 + 1/2 + 1/3 + ... + 1/n.'''

n = int(input("Enter the nth term: "))
sum = 0

for i in range(1, n+1):
    sum += 1/i
    print(f"1/{i} ", end="")
    if i < n:
        print(" + ", end="")

print("\nSum of the series: ", round(sum, 2))

'''
Output: 
Enter the nth term: 5
1/1  + 1/2  + 1/3  + 1/4  + 1/5 
Sum of the series:  2.28
'''