## 55. Write a program to show implementation of module using python program.

```python
# This file is named as 'calc.py'

def sum(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y
```

### NOTE: &nbsp; The both <b><em>calc.py</em></b> and <b><em>main.py</em></b> is stored in same folder.

```python
# This file is named as 'main.py'

from calc import *

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

print(f"The addition is: {sum(a,b)}")
print(f"The subtraction is: {sub(a,b)}")
print(f"The product is: {mul(a,b)}")
print(f"The quotient is: {div(a,b)}")
```

```
Output:

Enter 1st number: 15
Enter 2nd number: 10
The addition is: 25
The subtraction is: 5
The product is: 150
The quotient is: 1.5
```

### Jump to the actual folder 👉 <em><a href="https://github.com/atanu3000/college_assignments_python/tree/main/55_module"> click </a></em>