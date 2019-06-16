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
        return index
    else:
        index += 1
        return linear_search_recursive(array, item, index)
    # TODO: implement linear search recursively here
    pass
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # binary_search(array, item)
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


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
    # TODO: implement binary search recursively here
    print("")
#    print("looking for " + str(item) + " out of " + str(array[left: right]))
#    print("")
    if left == None and right == None:
        left = 0
        right = len(array)-1

    middle = math.floor((right + left)/2)

    if array[middle] == item:
        return middle
    else:
        if item < middle:
            binary_search_recursive(array, item, left, middle)
        else item > middle:
            binary_search_recursive(array, item, middle, right)

if __name__ == '__main__':
    linear_search([1,2,3,4,5,6,7], 5)
    # binary_search_recursive([1,2,3,4,5], 4)
