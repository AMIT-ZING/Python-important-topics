
def bSearch(list, key):
    lower = 0
    upper = len(list)-1

    while lower <= upper:
        global mid
        mid = (lower+upper)//2

        if list[mid] == key:
            return True
        else:
            if key < list[mid]:
                upper = mid - 1
            else:
                lower = mid + 1
    return False

myList = [1, 3, 4, 5, 8, 9]
myKey = 3

if bSearch(myList, myKey):
    print("Item found at place: {}".format(mid+1))
else:
    print("Item not found....")