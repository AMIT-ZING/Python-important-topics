# 3. functions can be returned by other functions:
def name(text):
    n = text

    def print_fn():
        print("My name is {}".format(n))

    return print_fn

intro = name("Amit")         # now intro = print_fn

intro()                      # since print_fn() doesn't take any arguments, intro() won't take any either

