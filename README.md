# Python-important-topics

## ITERATOR :
An iterator is a state so that it remembers where it is during iteration.  

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

#### How can we tell if something is iterable or not ? 
If something is iterable then it needs to have a special method "__iter__()" .  
To look at the attributes and methods available to an object we can use the following code :
```python
print(dir(list))
```

#### OUTPUT :
```
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__',
'__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index',
'insert', 'pop', 'remove', 'reverse', 'sort']
```
