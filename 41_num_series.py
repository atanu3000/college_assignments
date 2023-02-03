'''
41. WAP to calculate the sum of following series:
    1^1/1 + 2^2/2 + 3^3/3 + ... + n^n/n.'''

n = int(input("Enter the nth term: "))
sum = 0

for i in range(1, n+1):
    sum += i**i/i
    print(f"{i}^{i}/{i}", end="")
    if i < n:
        print(" + ", end="")

print("\nSum of the series: ", round(sum, 2))

'''
Output:
Enter the nth term: 5
1^1/1 + 2^2/2 + 3^3/3 + 4^4/4 + 5^5/5
Sum of the series:  701.0
'''