# 29. WAP to calculate sum of qubes from 1 to n number.

last_num = int(input("Enter the nth number: "))
ans = 0
for i in range(1, last_num+1):
    ans += i**3

print("The result is: ", ans)

# Output:
# Enter the nth number: 10
# The result is:  3025