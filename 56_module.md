## 56. WAP to show the implementation of name alicing in module using python program.

```python
# The file is named as 'my_module.py'

def greet():
    name = input("Enter your name: ")
    print(f'Hello {name}, Good morning!')
    print(f'This is from {__name__}')
```

```python
# The file is named as 'main.py'

from my_module import greet as abc

def greet():
    name = input("Enter your name: ")
    print(f'Happy Birthday {name}. God Bless you!\n')

greet()
abc()
```

```
Output:

Enter your name: Atanu
Happy Birthday Atanu. God Bless you!

Enter your name: Alan
Hello Alan, Good morning!
This is from my_module
```

### NOTE: &nbsp; The both <b><em>my_module.py</em></b> and <b><em>main.py</em></b> is stored in same folder.

### Jump to the actual folder 👉 <em><a href="https://github.com/atanu3000/college_assignments_python/tree/main/56_module"> click </a></em>