# 64. write a  program to swap two values using tuple asignment.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print ("a = ",a, "b = ",b)

(a,b) = (b,a)

print("a = ",a, "b = " ,b)

'''
Output:
Enter the first number: 10
Enter the second number: 20
a =  10 b =  20
a =  20 b =  10
'''