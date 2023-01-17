# 15. WAP to calculate the grade of a student on the basis of the marks of five subjects

a = int(input("Marks in Bengali:: "))
b = int(input("Marks in English:: "))
c = int(input("Marks in Math:: "))
d = int(input("Marks in Science:: "))
e = int(input("Marks in Computer:: "))

avg = (a + b + c + d + e) / 5

if avg >= 90:
    print("Outstanding")
elif avg >= 80 and avg < 90:
    print("Excellent")
elif avg >= 70 and avg < 80:
    print("Very good")
elif avg >= 60 and avg < 70:
    print("good")
elif avg >= 50 and avg < 60:
    print("Pass")
else:
    print("Fail")

# Output:
# Marks in Bengali:: 90
# Marks in English:: 85
# Marks in Math:: 98
# Marks in Science:: 82
# Marks in Computer:: 88
# Excellent