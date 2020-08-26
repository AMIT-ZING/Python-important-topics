# Closures:
First let us see the book definition of a closure,  
the method of binding data to a function without actually passing them as parameters is called closure. 
It is a function object that remembers values in enclosing scopes even if they are not present in memory.  

I know the definition is little difficult to understand specially for the new comers.  
Let us understand what closure actually is and for that lets see what is a nested function and a non-local variable.  

#### Nested functions:
A function defined inside another function is called a nested function.  

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
- `y` can be called a local variable for the nested function.
