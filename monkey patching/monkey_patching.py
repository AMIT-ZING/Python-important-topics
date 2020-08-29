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

greet = greetings(5, "hello", "bye")

print(greet.a)
greet.hello()
greet.bye()

def hi():
    print("hi there")

def goodbye():
    print("goodbye")

greet.hello = hi                   # monkey patching
greet.bye = goodbye                # monkey patching
greet.a = 10                       # monkey patching

print("\n")                        # to give a line space
print(greet.a)
greet.hello()
greet.bye()