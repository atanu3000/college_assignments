# 31. WAP to print a square star pattern.
    # * * * * * *
    # * * * * * *
    # * * * * * *
    # * * * * * *
    # * * * * * *
    # * * * * * *

row = int(input("Enter the row: "))
for i in range(row):
    for j in range(row):
        print("* ", end = "")
    print()

# Output:
# Enter the row: 6
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *