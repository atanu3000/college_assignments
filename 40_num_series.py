'''
40. WAP to calculate the sum of following series:
    1^2/1 + 2^2/2 + 3^2/3 + ... + n^2/n.'''

n = int(input("Enter the nth term: "))
sum = 0

for i in range(1, n+1):
    sum += i**2/i
    print(f"{i}^2/{i}", end="")
    if i < n:
        print(" + ", end="")

print("\nSum of the series: ", round(sum, 2))

'''
Output: 
Enter the nth term: 5
1^2/1 + 2^2/2 + 3^2/3 + 4^2/4 + 5^2/5
Sum of the series:  15.0
'''