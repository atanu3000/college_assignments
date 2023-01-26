# 30. WAP to calculate the sum of square of even number from 1 to 10.

sum = 0
for i in range(1, 11):
    if i % 2 == 0:
        sum += i**2

print("The result is: ", sum)