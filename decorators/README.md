# DECORATORS:
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.  

**To understand decorators, let's see what NESTED FUNCTIONS is:**  

#### Nested functions:
A function defined inside another function is called a nested function.  

e.g.  

```python
def abc():
    def xyz():
        print("this is an example of nested functions.....")
```

Here,  
- `xyz()` is the nested function.
- `abc()` is the enclosing function.   

**Now that's done, let's understand decorators with an example:**  

Let's make a decorator function,  

```python
def decorator(func):
    def wrapper():
        print("login action before calling func")
        func()
        print("actions after calling the func")
    return wrapper
```

As you can see there is a decorator function (decorator()) with func as an argument and under it there is a nested function (wrapper()).  
The decorator function is returning the wrapper function.  

Let's make the function to be decorated,  

```python
def welcome_msg():
    print("WELCOME BACK")
```

Now let's make an instance of the decorator function with `welcome_msg` function as an argument and call the instance function,    

```python
welcome_msg = decorator(welcome_msg)              # we are keeping the instance name same as the function name

welcome_msg()
```

**OUTPUT:**  

```
login action before calling func
WELCOME BACK
actions after calling func
```

The decorator function takes the function to be decorated(welcome_msg) as an argument.  

Now let's understand where and how the decorator function is working here,

Suppose we need to add some functionality to our `welcome_msg()` function without disturbing its structure (or preserving its own functionality).  
To make it easy suppose we need the function `welcome_msg()` to only work after the user logs in. We simply need to make a decorator for the login function and pass our original function to the decorator function as shown in the example. It will add the functionality `login` to our original function. Now without complete execution of the additional functionality (login action), the original function won't get executed. So this is how we can add an action or functionality to any function.  

Now you must have seen something like `@decorator`,  
This is nothing but same as writting `welcome_msg = decorator(welcome_msg)`. You can write `welcome_msg = decorator(welcome_msg)` or add `@decorator` on top of your function. It will give the same result plus it makes it easy to apply a decorator and ya it looks cool as well.   

```python
@decorator
def welcome_msg():
    print("WELCOME BACK")
```

**OUTPUT:**  

```
login action before calling func
WELCOME BACK
actions after calling func
```

*NOTE: You can also apply multiple decorators to a function*

  


