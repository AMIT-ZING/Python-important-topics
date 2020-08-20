# Pass by reference v/s pass by value in Python:

### Is Python Argument Passing model a “Pass by Value” or “Pass by Reference”? :
You might be surprised to know that the Python’s argument passing model is neither “Pass by Value” nor “Pass by Reference” but it is “Pass by Object Reference”.

**First let us see the difference between "pass/call by value" and "pass/call by reference"**  

### Pass/call by value:
In "pass by value", the function receives a copy of the argument object passed to it by the calling statement and it is stored in a new location in memory. 
Passing values of parameter to the function, if any kind of change is done to those parameters inside the function, those changes are not reflected back in the actual argument object.  
That means the original object stays intact and all changes made are to a copy of the same and stored at different memory locations.

#### e.g.
```python
def print_val(x):
    x = 333
    print(x)
    return x

y = 222
print_val(y)
print(y)
```
**OUTPUT:**
```
333
222
```

When we run the program first of all it creates a variable `y = 222` then it comes to the line `print_val(y)` which calls the function. 
Here the caller is provided with the argument "y" hence a copy of the argument object(y = 222) is sent to the function. 
Now whatever changes the function does on the copy object is stored in another memory location which doesn't affect the original object. 
Hence the statement `print(x)` prints `333` as it is instructed(changing the value to 333) by the function and the `print(y)` statement prints `222` which is the original value as you can see.

### pass/call by reference:
In "pass by reference", the function receives a reference to the argument objects passed to it by the caller and both(the reference and the object) pointing to the same memory location.  
Passing reference of parameters to your function, if any change is done to those parameters inside the function, those changes get reflected back to the actual argument object. 
That means the original object changes as well as the reference object sent to the function and are stored in the same memory location. 

```python
def show_val(x):
    x[0] = 222
    print(x)
    return x

a = [1, 2, 3, 4]
show_val(a)
print(a)
```
**OUTPUT:**
```
[222, 2, 3, 4]
[222, 2, 3, 4]
```

When we run the program first of all it creates a list `a = [1, 2, 3, 4]` then it comes to the line `show_val(y)` which calls the function. 
Here the caller is provided with the argument "a" hence a reference to the argument object(a = [1, 2, 3, 4]) is sent to the function. 
Now whatever changes the function does on the reference object is stored in the same memory location as the original object plus the original object also gets changed. 
Hence the statement `print(x)` prints `[222, 2, 3, 4]` as it is instructed(changing the value of x[0] to 222) by the function and the `print(y)` statement also prints `[222, 2, 3, 4]` which is the changed value as you can see.

## Pass/call by object reference:





