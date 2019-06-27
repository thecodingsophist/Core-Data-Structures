#!python
import math

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_recursive(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # the time complexity for this is O(N)
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # the time complexity for this is O(N)
    if item == array[index]:
        print("index", index)
        return index
    elif index == len(array) - 1:
        return None
    else:
        index += 1
        return linear_search_recursive(array, item, index)

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # binary_search(array, item)
    # return binary_search_iterative(array, item)
    index = binary_search_recursive(array, item)
    print(index)
    return index


def binary_search_iterative(array, item):
    # the time complexity for this is O(logN)
    # TODO: implement binary search iteratively here

    first = array[0]
    last = array[len(array)-1]
    middle = array[int(math.ceil(len(array)/2))]

    for n in array:
        if middle == item:
            return int(math.ceil(len(array)/2))
        elif item > middle:
            first = middle
        elif item < middle:
            last = middle

    return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # the time complexity for this is O(logN)
    # implement binary search recursively here

    if left == None and right == None:
        left = 0
        right = len(array)-1

    # where middle is the index of the middle items
    # calculated using the right and left index at each recursive call
    middle = (right + left)//2

    if item == array[middle]:
        print("index of item: ", middle)
        return middle
    # if the item is not found in the list
    elif left == middle or right == middle:
        print("the item is not found in the list")
        return None
    else:
        if item < array[middle]:
            result = binary_search_recursive(array, item, left, middle - 1)
            return result
        else:
            result = binary_search_recursive(array, item, middle + 1, right)
            return result

if __name__ == '__main__':
    # linear_search([1,2,3,4,5,6,7], 5)
    # names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    # binary_search_recursive(names, 'Alex')

    names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    # binary search should return the index of each item in the list
    assert binary_search(names, 'Winnie') == 6
