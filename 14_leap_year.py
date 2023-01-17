# WAP a program to wheather a year is leap year or not.

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not leap year")
    2016

# Output:
# Enter a year: 2016
# Leap year