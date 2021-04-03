 # map() FUNCTION

The map() function executes a specified function for each item in an iterable. With map() function we can apply a particular function on each element of the list without using loops.

### Syntax :
```
map(function, iterable)
```
for example,  

## Example 1 :

```python
def addition(n):
    return n + n

numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
```
#### OUTPUT :
```
[2, 4, 6, 8]
```
## Example 2 :

```python
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))
```
#### OUTPUT :
```
[2, 4, 6, 8]
```

## Example 3 :

```python
numbers1 = [0, 1, 9]
numbers2 = [4, 5, 6]
  
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))
```
#### OUTPUT :
```
[4, 6, 15]
```

## Example 4 :
```python
l = ['abc', 'def', 'geh']

test = map(list, l)
print(list(test))
```
#### OUTPUT :
```
[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'e', 'h']]
```

 # filter() Function

The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

### Syntax :
```
filter(function, iterable)
```
## Example 1 :

```python
animals = ["cat", "dog", "tiger", "lion", "cow", "elephant"]

def herbivores(name):
    if name in animals:
        return True
    else:
        return False

herbivorous = ["cow", "elephant", "zebra"]
herb_animals = filter(herbivores, herbivorous)

print(list(herb_animals))
```
#### OUTPUT :
```
['cow', 'elephant']
```
It filters elements from the given list according to the function defined.

## Example 2 :
```python
seq = [0, 1, 2, 3, 5, 8, 13]

result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

result = filter(lambda x: x % 2 == 0, seq)
print(list(result))
```
#### OUTPUT :
```
[1, 3, 5, 13]
[0, 2, 8]
```

# reduce() Function

The reduce() method executes a given reducer function on each element of the array, resulting in single output value.
This function is defined in “functools” module.

## Syntax :
```
reduce(function, iterable)
```

## Example 1 :

```python
import functools

list = [ 1 , 3, 5, 6, 2, ]

print("sum of the elements of the given list is :")
print(functools.reduce(lambda a,b : a+b,list))
```
#### OUTPUT :
```
sum of the elemens in the list is : 
17
```

## Example 2 :

```python
import functools

l = [ 1 , 3, 5, 6, 2, ]

print ("The maximum element of the list is : ")
print (functools.reduce(lambda a,b : a if a > b else b, l))
```
#### OUTPUT :
```
The maximum element of the list is : 
6
```

# accumulate() Function :

accumulate() returns a iterator containing the intermediate results.
This function is defined in "itertools" madule.

## Example :

```python
import itertools

l = [ 1, 3, 4, 10, 4 ]

print ("The summation of list using accumulate is :")
print (list(itertools.accumulate(l,lambda x,y : x+y)))
```

#### OUTPUT :
```
The summation of list using accumulate is :
[1, 4, 8, 18, 22]
```

# zip() Function :

The zip() function returns an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together and then pairing the third item and so on....  

## Syntax :
```
zip(iterator1, iterator2, iterator3 ...)
```

## Example 1 :
```python
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9]

z = zip(x, y)

print(list(z))
```
#### OUTPUT :
```
[(1, 6), (2, 7), (3, 8), (4, 9)]
```

## Example 2 :
```python
girls = ["Mahathi", "priya", "kazal"]

boys = ["Ram", "Shyam", "Rohan"]

couples = zip(boys, girls)

print(list(couples))
```
#### OUTPUT :
```
[('Ram', 'Mahathi'), ('Shyam', 'priya'), ('Rohan', 'kazal')]
```







