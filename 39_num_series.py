'''
39. WAP to calculate the sum of following series:
    1 + 1/2^2 + 1/3^2 + ... + 1/n^2.'''

n = int(input("Enter the nth term: "))
sum = 0

for i in range(1, n+1):
    sum += 1/i**2
    print(f"1/{i}^2 ", end="")
    if i < n:
        print(" + ", end="")

print("\nSum of the series: ", round(sum, 2))

'''
Output: 
Enter the nth term: 5
1/1^2  + 1/2^2  + 1/3^2  + 1/4^2  + 1/5^2
Sum of the series:  1.46
'''