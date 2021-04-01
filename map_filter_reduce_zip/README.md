# map() FUNCTION

The map() function executes a specified function for each item in an iterable. With map() function we can apply a particular function on each element of the list without using loops.

### Syntax :
```
map(fun, iter)
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







