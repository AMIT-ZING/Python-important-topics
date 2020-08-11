# Python-important-topics

## ITERATOR :
An iterator is a state so that it remembers where it is during iteration.  
An iterator also knows to get its next value as it remembers its previous value.  
An iterator gets its next value using the method "__next__()" .

## ITERABLE :
Iterables are something that can be looped over.  
### e.g.
A list can be called iterable as we can loop over a list.  

```python
list = [1, 2, 4, 6, 7]

for i in list:
    print(i)
```    
#### OUTPUT :
```
1
2
4
6
7
```

### How can we tell if something is iterable or not ? 
If something is iterable then it needs to have a special method "__iter__()" .  
To look at the attributes and methods available to an object we can use the following code :
```python
print(dir(list))
```

#### OUTPUT :
```
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__',
'__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__ iter __', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index',
'insert', 'pop', 'remove', 'reverse', 'sort']
```

Here the list has the "__iter__" method hence the list is iterable. 
The list is iterable but it is not an iterator.  
To make the list an iterator we need to run "__iter__()" method on our list.

```python
i_list = list.__iter__()
```

This makes the list an iterator.

### How can we tell if something is an iterator or not ?
If something is an iterator then it needs to have the special method "__next__()" .  
we can check it by passing the list into the `dir()` function :

```python
print(dir(I_list))
```

#### OUTPUT :
```
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
'__le__', '__length_hint__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__',
'__subclasshook__']
```
Here we have the `__next__` method. Hence the list has become an iterator.  
The `next() or __next__()` method returns the next value and it also remembers where it left off last time.  

```python
    print(next(i_list))
    print(next(i_list))
    print(next(i_list))
    print(next(i_list))
    print(next(i_list))
```

#### OUTPUT :
```
1
2
4
6
7
```

*NOTE: Integers are not iterable*

### Looping through an iterator :
#### e.g.
```python
list = ["apple", "banana", "mango"]

for i in list:
    print(i)
```
#### OUTPUT :
```
apple
banana
mango
```

Here the `for in` loop automatically creates an iterator object and executes the next() method for each loop.

