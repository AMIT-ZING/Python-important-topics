# First class functions:
In computer science, a programming language is said to have first-class functions if it treats functions as first-class citizens. 
This means the language supports passing functions as arguments to other functions, returning them as the values from other functions, 
and assigning them to variables or storing them in data structures.  

We can say that a function in Python is First Class Function, if it supports all of the properties of a First Class object.

## Properties of first class functions:
- A function is an instance of the Object type.
- You can store the function in a variable.
- You can pass the function as a parameter to another function.
- You can return the function from a function.
- You can store them in data structures such as hash tables, lists, …

### You can store the function in a variable:
In python, functions can be stored in variables.  

**e.g.**  

Let us make a function `func1()` with an argument "text"

```python
def func1(text):
    print(text)
```

Assigning the function to a variable:
```python
variable = func1
```

*NOTE: giving `()` at the time of assigning will execute the function but if you assign the function without `()` then it only assigns the function to the variable without executing it*  

Calling the function:  
```python
variable("My name is Amit")
```

Here function takes an argument and since `variable = function`, the variable will take an argument at the time of calling it.  

**OUTPUT:**  
```
My name is Amit
```

### You can pass the function as a parameter to another function:

In python, functions can be given as arguments to other functions.  

**e.g.**  

First lets define a function to be passed as the parameter,  

```python
def intro(text):
    print(text)
```

Now lets make another function where the first function is gonna be passed as an argument,  

```python
def print_fn(func, text):
    func(text)
```
Here `func` is passed as an argument.  
Now lets call the `print_fn` function,

```python
print_fn(intro, "My name is Amit")
```

Here the `intro()` function is given as a parameter to the `print_fn()` function.  

**OUTPUT:**  

```
My name is Amit
```

### You can return the function from a function:

In python, a function can be used as a return statement for another function.  

**e.g.**  

Lets see an example,  

```python
def name(text):
    n = text

    def print_fn():
        print("My name is {}".format(n))

    return print_fn
```

Here the inner function is being used as a return statement for the outer function.

```python
intro = name("Amit")
```

Now the outer function has been assigned to the variable `intro`.  
We are gonna call the function with the help of the variable `intro`,

```python
intro()
```

**OUTPUT:**  

```
My name is Amit
```
