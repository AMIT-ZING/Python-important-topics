# Monkey Patching:
Monkey patching is a technique that allows you to alter the behavior of objects or add objects to a class at runtime.  
Now it is very useful only if you use it carefully, if used carelessly it will make your code complicated and difficult to debug.  

let's see an example to understand `Monkey patching` more clearly,  

e.g.  

Let's make a class `greetings` and some methods in it,  

```python
class greetings:
    a = 0
    b = ""
    c = ""

    def __init__(self, anyNumber, text1, text2):
        self.a = anyNumber
        self.b = text1
        self.c = text2

    def hello(self):
        print(self.b)

    def bye(self):
        print(self.c)
```

Here we created some variables and two methods in the class,  
variables: `a`, `b` and `c`  
methods: `hello()` and `bye()`  

Let's create an instance for the class and call the methods,  

```python
greet = greetings(5, "hello", "bye")

print(greet.a)
greet.hello()
greet.bye()
```
**OUTPUT:**
```
5
hello
bye
```

Now suppose we need to change the behaviour of some method of the class at runtime for some specific purpose.  
Let's make some functions with the required functionality,  

```python
def hi():
    print("hi there")

def goodbye():
    print("goodbye")
```

As you can see we don't need to give any arguments like `self` as the functions are not a part of the class.  
*NOTE: You can give other arguments if the functionality of the function requires it*

Now let's assign these functions to the methods we need to change the behaviour of, and again call the methods,  

```python
greet.hello = hi                   # monkey patching
greet.bye = goodbye                # monkey patching
greet.a = 10                       # monkey patching

print(greet.a)
greet.hello()
greet.bye()
```
**OUTPUT:**  
```
10
hi there
goodbye
```

You can see, we have the new output as we wanted and we did in at runtime.  

## Why to use it ?
Suppose you made a library in python but now you need an object of the library to show a different functionality (different behaviour) then what will you do. Will you go and mess with the object in the library. It may create some other bugs in the library and it'll take more time. Under such situations monkey patching comes in play. You can just alter the behaviour of the object at runtime using monkey patching technique.

*NOTE: If the object is mutable, monkey patching will alter the original object (no new memory location will be assigned), but if the object is immutable, monkey patching will just assign a new memory location to the altered object*






