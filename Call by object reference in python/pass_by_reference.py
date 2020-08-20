def show_val(x):
    x[0] = 222
    print(x)
    return x

a = [1, 2, 3, 4]
show_val(a)
print(a)