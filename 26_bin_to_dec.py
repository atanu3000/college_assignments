# 26. WAP to calculate decimal equivalent of the binary number given by user.

bin = int(input("Enter the binary digit: "))
dec = 0
i = 0
while bin > 0:
    r = bin % 10
    dec += r * 2**i
    bin //= 10
    i += 1

print("The equivalent decimal: ", dec)

# Output:
# Enter the binary digit: 1101
# The equivalent decimal:  13