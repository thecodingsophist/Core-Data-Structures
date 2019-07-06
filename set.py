from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        self.container = HashTable()
        self.size = 0
        if elements:
            for element in elements:
                self.container.set(element,1)
                self.size+=1

    def contains(self, element):
        """Best time complexity: O(1
        Worst time complexity: O(n)"""
        return self.container.contains(element)

    def add(self, element):
        """Best time complexity: O(1
        Worst time complexity: O(n)"""
        if not self.contains(element):
            self.container.set(element,1)
            self.size += 1

    def remove(self, element):
        """Best time complexity: O(1
        Worst time complexity: O(n)"""
        if self.contains(element):
            self.container.delete(element)
            self.size -= 1
        else:
            raise KeyError("Element not in set.")

    """For space and time complexity: Let
    n = size of set 
    m = size of other set
    l = size of new set"""

    def union(self, other_set):
        """Time complexity: O(n+(m-m&n))
        Space complexity: O(l+m)"""
        new_set = Set()
        other_set_copy = other_set
        for element in self.container.keys():
            if other_set_copy.contains(element):
                other_set_copy.container.delete(element)
            new_set.add(element)
        for element in other_set_copy.container.keys():
            new_set.add(element)
        return new_set

    def intersection(self, other_set):
        """Time complexity: O(n) or O(m), whichever one is smaller.
        Space complexity: O(l)"""
        new_set = Set()# O(b)
        if self.size > other_set.size:
            # check to see which set is smaller and then iterate through that one.
            for element in other_set.container.keys():# O(m)
                if self.contains(element):# O(1)
                    new_set.add(element)# O(1)
        else:
            for element in self.container.keys(): # O(n)
                if other_set.contains(element):# O(1)
                    new_set.add(element)# O(1)
        return new_set

    def difference(self, other_set):
        """
        Time complexity: O(n)
        Space complexity: O(n-n&m)"""
        new_set = Set()
        for element in self.container.keys(): #O(n)
            # iterate throuh the elements in .keys()
            if not other_set.contains(element):# O(1)
                new_set.add(element)# O(1)
        return new_set

    def is_subset(self, other_set):
        """Time complexity: O(m)
        Space complexity: O(1)"""
        if self.size > other_set.size:
            for element in other_set.container.keys():
                if not self.contains(element):
                    return False
            return True
        else:
            return False
