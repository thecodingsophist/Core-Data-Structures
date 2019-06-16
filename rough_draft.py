# TAKE TWO ON BINARY_SEARCH_RECURSIVE

    #BASE CASE
    if len(new_array) == 0:
        print("item not in list")
        return None
    elif item == new_array[middle]:
        print("iteration = " + str(iteration))
        index = 2**iteration + middle
        print("index = " + str(index))
        print(array[index])
        return array[index]
    else:
        new_iteration = iteration + 1
        #IF ARRAY IS ODD
        if len(new_array)%2 == 1:
            if item > new_array[middle]:
                print("case 1")
                print("now, array is " + str(array) + " left is " + str(left) + " right is " + str(right))
                print("and new_array is " + str(new_array))
                binary_search_recursive(array, item, new_iteration, left = 2**iteration + middle+1, right = None)
            else:
                print("case 2")
                print("now, array is " + str(array) + " left is " + str(left) + " right is " + str(right))
                print("and new_array is " + str(new_array))
                binary_search_recursive(array, item, new_iteration, left = 0, right = middle)
        #ELSE IF ARRAY IS EVEN
        else:
            if item > new_array[middle]:
                print("case 3")
                print("now, array is " + str(array) + " left is " + str(left) + " right is " + str(right))
                print("and new_array is " + str(new_array))
                binary_search_recursive(array, item, new_iteration, left = 2**iteration + middle, right = None)
            else:
                print("case 4")
                print("now, array is " + str(array) + " left is " + str(left) + " right is " + str(right))
                print("and new_array is " + str(new_array))
                binary_search_recursive(array, item, new_iteration, left = 0, right = middle)

# TAKE ONE ON BINARY_SEARCH_RECURSIVE

def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    print("")
    array = array[left: right]
    print(array)
    index = int(math.ceil((len(array)-1)/2))
    print("len(array) = " + str(len(array)))
    print("index = " + str(index))

    if index == -1:
        print("item not in list")
        return None

    middle = array[index]

    if len(array) == 0:
        print("item not in list")
        return None
    elif item == middle:
        print(index)
        return index
    elif item > middle:
        print("===========item is greater than middle========= " + str(middle))
        print("+++++++++++++++left is++++++++++++++++" + str(left))
        print("+++++++++++++++right is+++++++++++++++" + str(right))
        print("dude, the array is " + str(array))

        binary_search_recursive(array, item, middle, -1)
    elif item < middle:
        print("===========item is less than middle========= " + str(middle))
        print("+++++++++++++++left is++++++++++++++++" + str(left))
        print("+++++++++++++++right is+++++++++++++++" + str(right))
        print("dude, the array is " + str(array))

        binary_search_recursive(array, item, 0, middle)

# TAKE TWO! SPOILER ALERT: DOESN'T WORK DUE TO NEED FOR AN OG ARRAY

def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    print("")
    print("looking for " + str(item) + " out of " + str(array))
    print("")

    iteration = 0
    middle = math.floor(len(array)/2)
    print("middle = " + str(middle))

    #BASE CASE
    if len(array) == 0:
        print("item not in list")
        return None
    elif item == array[middle]:
        index = 2**iteration + middle
        print(array[index])
        return array[index]
    else:
        iteration += 1
        #IF ARRAY IS ODD
        if len(array)%2 == 1:
            if item > array[middle]:

                binary_search_recursive(array[middle+1: -1], item, iteration)
            else:
                binary_search_recursive(array[0: middle-1], item, iteration)
        #ELSE IF ARRAY IS EVEN
        else:
            if item > array[middle]:
                binary_search_recursive(array[middle: -1], item, iteration)
            else:
                binary_search_recursive(array[0: middle], item, iteration)
