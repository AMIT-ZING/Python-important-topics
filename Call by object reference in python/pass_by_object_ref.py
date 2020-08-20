# immutable object example
def print_val(x):
    x = 3
    print(x, id(x))
    return x

y = 2
print_val(y)
print(y, id(y))
print("\n")

# mutable object example
def show_val(x):
    x[0] = 222
    print(x, id(x))
    return x

a = [1, 2, 3, 4]
show_val(a)
print(a, id(a))
