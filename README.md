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
print(dir(num))
```
