from set import Set
import unittest


class SetTest(unittest.TestCase):

    def test_contains(self):
        new_set = Set(['h','e','y',1,2])
        assert new_set.contains('h') == True
        assert new_set.contains('e') == True
        assert new_set.contains('y') == True
        assert new_set.contains(1) == True
        assert new_set.contains(3) == False
        assert new_set.size == 5

    def test_add(self):
        new_set = Set(['h'])
        new_set.add('e')
        new_set.add('y')
        new_set.add(1)
        new_set.add(2)
        assert new_set.contains('h') == True
        assert new_set.contains(1) == True
        assert new_set.contains('e') == True
        assert new_set.size == 5


    def test_remove(self):
        new_set = Set(['h','e','y',1,2])
        assert new_set.size == 5
        new_set.remove("h")
        new_set.remove("e")
        new_set.remove("y")
        assert new_set.contains('h') == False
        assert new_set.contains("e") == False
        assert new_set.contains('y') == False
        assert new_set.size == 2

    def test_union(self):
        new_set = Set(['h','e','y',1,2])
        other_set  = Set(['u',1,2,7])

        union_set = new_set.union(other_set)

        assert union_set.contains(2) == True
        assert union_set.contains('u') == True
        assert union_set.contains(1) == True
        assert union_set.contains("!") == False

    def test_intersection(self):
        new_set = Set(['h','e','y',1,2])
        other_set  = Set(['u',1,2,7])

        intersection_set = new_set.intersection(other_set)


        assert intersection_set.contains(2) == True
        assert intersection_set.contains(1) == True
        assert intersection_set.contains('u') == False
        assert intersection_set.contains("!") == False

    def test_difference(self):
        new_set = Set(['h','e','y',1,2])
        other_set  = Set(['u',1,2,7])

        difference_set = new_set.difference(other_set)

        assert difference_set.contains(1) == False
        assert difference_set.contains('h') == True
        assert difference_set.contains(2) == False
        assert difference_set.size == 3

    def test_is_subset(self):
        new_set = Set(['h','e','y',1,2])
        other_set  = Set([1,2])

        assert new_set.is_subset(other_set) == True

        new_set = Set(['h','e','y',1,2])
        other_set  = Set(['y'])

        assert new_set.is_subset(other_set) == True

        new_set = Set(['h','e','y',1,2])
        other_set  = Set(['j', 'k'])

        assert new_set.is_subset(other_set) == False
