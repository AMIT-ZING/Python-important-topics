# Closures:
First let's see the book definition of a closure,  
the method of binding data to a function without actually passing them as parameters is called closure. 
It is a function object that remembers values in enclosing scopes even if they are not present in memory.  

I know the definition is little difficult to understand specially for the new comers.  
Let's understand what closure actually is and for that lets see what is a nested function and a non-local variable.  

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

#### Non-local variables:
Nested functions can access variables of the enclosing scope/function. These variables are called non-local variables as they are not local to the inner/nested function.  

**e.g.**  

```python
def number(x):              # outer function or enclosing function

    def increase_by(y):     # inner function or nested function
        print(x + y)
    
    return increase_by      # return statement
```

Here,  
- `number(x)` is the enclosing function or scope.
- `increase_by(y)` is the nested/inner function.
- `x` is the non-local variable since nested function can access the variable defined in the enclosing scope.
- `y` can be called a local variable to the nested function.  

**Coming back to `closures`,**  
Let's look at an example to understand it clearly,  

```python
def number(x):                             # outer function or enclosing function

    def increase_by(y):                    # inner function or nested function
        print(x + y)
    
    return increase_by                     # return statement

add = number(5)                            # now "add" is equal to the returned function i.e. add = increase_by(y)

add(7)                                     # giving add a parameter since increase_by() takes an argument "y"
```
**OUTPUT:**
```
12
```

Here the nested function(`increase_by()`) is being returned to the outer function. The outer/enclosing function is called with the parameter `5` and the nested function(`increase_by()`) is bound to the `add` variable. Hence the execution of the outer/enclosing function is done.  
Now on calling `add(7)`, the execution is done without any problems, means `add()` remembered the variable `x` even after the execution of the enclosing function(`number()`) is already finished.  

(*NOTE: the functionality of the nested/inner function depends on the variable of the outer function. i.e. `increase_by()` depends on non-local variable `x`*)  

In other words the interpreter remembered the variable `x` in case the outer function goes away(finishes executing or gets deleted), **this technique of remembering some data is called CLOSURE**  

e.g.  

```python
del number        # to delete the outer function

add(7)

number(5)         # calling the deleted outer function
```
**OUTPUT:**
```
12

Traceback (most recent call last):
  File "d:/python (spyder)/Python (important topics)/closures.py", line 16, in <module>
    number(5)
NameError: name 'number' is not defined
```

As you can see `add` still gives an output even after `number()` got deleted(and with it the the variable `x` got deleted as well)




