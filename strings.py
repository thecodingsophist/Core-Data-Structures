#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    """Time Complexity: O(n), the best case is finding the pattern in the text
    in the beginning, the worst case is going through the entire text and finding
    the text at the end."""
    """Space Complexity: O(n)"""

    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement contains here (iteratively and/or recursively)
    length = len(pattern)
    # print('length =', length)
    if len(text) < len(pattern):
        raise ValueError('pattern is longer than the text length')
    index = 0
    while index < len(text) + 1 - length:
        # print("maybe text = " + text[index: index+(length)])
        if text[index: index+(length)] == pattern or pattern == "":
            # print("True")
            return True
        index += 1
    # print("False")
    return False

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    """Time Complexity = O(n*m) where n is the length of the pattern and m is the length of the splices"""
    """Space Complexity = O(n)"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_index here (iteratively and/or recursively)
    if contains(text, pattern):
        length = len(pattern)
        index = 0
        while index < len(text) + 1 - length:
            # print("maybe text = " + text[index: index+(length)])
            # CHALLENGE: consider avoiding slicing text to save time and memory
            if text[index: index+(length)] == pattern or pattern == "":
                print('index at find_index =', index)
                return index
            index += 1
    else:
        return None

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    """Time Complexity = O(n^2*m) where n is the length of the pattern and m is the length of the splices"""
    """Space Complexity = O(n)"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    starting_indices = []
    left = 0
    while len(text[left:]) >= len(pattern):
        starting_index = find_index(text[left:], pattern)
        if starting_index == None:
            break
        starting_indices.append(left + starting_index)
        if left == len(text):
            break
    return starting_indices

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    # find_index("bananas", "nas")
    main()
