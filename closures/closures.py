# closures :

def number(x):              # outer function or enclosing function

    def increase_by(y):     # inner function or nested function
        print(x + y)
    
    return increase_by      # return statement

add = number(5)             # now add is equal to the returned function i.e. increase_by(y), add = increase_by(y)

add(7)                      # giving add a parameter since increase_by() takes an argument "y"