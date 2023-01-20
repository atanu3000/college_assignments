# 22. WAP to check wheather a number is prime or not

num = int(input("Enter a number: "))

flag = True

for n in range(2, num):
    # print(f"{num} % {n} = ", num % n)     <- Not use this line ->
    if num % n == 0:
        flag = False
        break

if flag == False:
    print(f"{num} is not prime")
else:
    print(f"{num} is prime")

# Output:
# Enter a number: 37
# 37 is prime
