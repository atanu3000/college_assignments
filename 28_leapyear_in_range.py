# 28. WAP that displays the leap years from 1900 to 2023.

print("All leap years from 1900 to 2023")
for i in range(1900, 2024):
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        print(i, " is leap year")

# Output:
# All leap years from 1900 to 2023
# 1904  is leap year
# 1908  is leap year
# 1912  is leap year

# ...

# 2020  is leap year