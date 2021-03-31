# LIST COMPREHENSION
`List Comprehension` is used to create/iterate list with a single line code.

First let's see the usual way of creating a list in python.

```python
list = []

for item in range(10):
    list.append(item)

print(list)
```
### OUTPUT :
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Now let's try the same thing with list comprehention.

```python
list = [item for item in range(10)]

print(list)
```
### OUTPUT :
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Here we got the same output with just a single line code. This is list comprehension.  

> ## SYNTAX :
### SYNTAX  
```
list = [<expression> for <item> in <iterable>]
```
```
list = [<expression> for <item> in <iterable> if <condition>]
```
```
list = [<expression> for <item> in <iterable> if <condition 1> and if <condition 2>]
```
```
list = [<expression> for <item 1> in <iterable 1> and for <item 2> in <iterable 2>]
```

> ## Iteration with list comprehension :  
` `  
Let's take a list of integers in range of 0 to 20.
```
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```

Now we will make a list in which the elements are divisible by 5 by iterating the elements of the above list.  
Let's do it first without the list comprehension.

```python
newList = []

for item in list:
    if item % 5 == 0:
        newList.append(item)

print(newList)
```

### OUTPUT :
```
[0, 5, 10, 15]
```

Now we will try it with list comprehension.

```python
newList = [item for item in list if item % 5 == 0]
```

### OUTPUT :
```
[0, 5, 10, 15]
```


