# 19. WAP to take a number between 1 to 7 from user and print corresponding day of week.

day = int(input("Enter a day between 1 to 7:: "))

if day == 1:
    print("Sunday")
elif day == 2:
    print("Monday")
elif day == 3:
    print("Tuesday")
elif day == 4:
    print("Wednesday")
elif day == 5:
    print("Thursday")
elif day == 6:
    print("Friday")
elif day == 7:
    print("Saturday")
else:
    print("Not a valid day")

# Output:
# Enter a day between 1 to 7:: 6
# Friday