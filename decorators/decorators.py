def decorator(func):
    def wrapper():
        print("blah blah action before calling func")
        func()
        print("blah blah action after calling func")
    return wrapper

@decorator
def welcome_msg():
    print("WELCOME BACK")

# welcome_msg = decorator(welcome_msg)          # or write @decorator on top of the function

welcome_msg()