mid = 0

def bSearch(list, key):
    lower = 0
    upper = len(list)-1           # the positioning starts from 0 that's why 1 is being subtracted

    while lower <= upper:
        global mid
        mid = (lower+upper)//2        # to find the mid position

        if list[mid] == key:          # if the "mid position element" = "item to be searched" then the function will return true and terminate
            return True
        else:
            if key < list[mid]:
                upper = mid - 1
            else:
                lower = mid + 1
    return False

myList = [1, 3, 4, 5, 8, 9]              # list provided by the user
myKey = 3                                # item to be searched

if bSearch(myList, myKey):
    print("Item found at place: {}".format(mid+1))          # print stmt if the function returns true
else:
    print("Item not found....")                             # print stmt if the function returns false