# 60. WAP to program to valuidate information by using string function.

name = input("Enter your name: ")

if name.isalpha() == False:
    print("Name Invalid")
else:
    pan = input("Enter pan number: ")
    if pan.isalnum() == False:
        print("Invalid pan number")

    else:
        print(f"Please check {name}, Your pan number is: {pan}")

'''
Output:
Enter your name: Atanu
Enter pan number: EAPP3443
Please check Atanu, Your pan number is: EAPP3443
'''