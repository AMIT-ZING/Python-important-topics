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

**OUTPUT**  
```
My name is Amit
```
