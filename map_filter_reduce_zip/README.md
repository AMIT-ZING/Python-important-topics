> # map() FUNCTION

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

> # filter() Function

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




