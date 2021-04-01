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

> ## list comprehebsion with if-else condition  
` `  
Let's do an example,  

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

fruits_2 = []

for fruit in fruits:
    if fruit == "banana":
        fruits_2.append("orange")
    else:
        fruits_2.append(fruit)

print(fruits_2)
```
### OUTPUT :
```
['apple', 'orange', 'cherry', 'kiwi', 'mango']
```
Here in this example we replaced `banana` with `orange` using an if else statement.  
now we will try the same with list comprehension.

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

fruits_2 = [fruit if fruit != "banana" else "orange" for fruit in fruits]

print(fruits_2)
```
### OUTPUT :
```
['apple', 'orange', 'cherry', 'kiwi', 'mango']
```
Let's understand this comprehention.  

```
fruits_2 = [fruit if fruit != "banana" else "orange" for fruit in fruits]
              ^   -------------------  ------------  -------------------
              |            |                 |                |
         (expression)      |                 |      (for loop to iterate items of the list)
                           |                 |
                           |       (else insert "orange" i.e. if fruit is equal to banana then insert "orange" in place of "banana")
                           |
                           |
    (if fruit is not equal to "banana" then do nothing)
```

> ## Nested list comprehention
Let's see an example,  

```python
matrix = []

for i in range(4):
    matrix.append([])  # inserting empty sublist 6 number of times
    for n in range(4):
        matrix[i].append(n)  # inserting numbers into the empty sublist

print(matrix)
```
### OUTPUT :
```
[[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]
```
Now the same thing wit `list comprehention`,
```python
matrix = [[n for n in range(4)] for _ in range(4)]
print(matrix)
```
### OUTPUT :
```
[[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]
```


