# 2. functions can be passed as arguments to other functions:
def func1(text):
    print(text)

def func2(text):
    print(text)

def print_fn(func, text):
    func(text)

print_fn(func1, "My name is Amit")           # func1 is passed as an argument in 'print_fn()' function

print_fn(func2, "My name is Sumit")          # func2 is passed as an argument in 'print_fn()' function
