#!python
import math
import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)

def is_palindrome_iterative(text):
    text = text.lower()
    left = 0
    right = len(text) - 1
    # while index < math.floor(len(text)/2):
    while left <= right:
        if not text[left].isalpha():
            left += 1
            continue
        if not text[right].isalpha():
            right -= 1
            continue
        # we use -(index + 1) because index at -0 is still 0, when trying
        # to get the end of the string, we have to use -1 to access it
        # so if we use index = 0 to begin with, we have to subtract 1 from it
        # hence the -(index+1) index for the last letter in the string
        if text[left] == text[right]:
            left += 1
            right -= 1
            continue
        else:
            return False
    return True

# def is_palindrome_recursive(text, left=None, right=None):
#     # text.lower()
#     if left == None and right == None:
#         left = 0
#         right = -1
#     if left > math.floor(len(text)/2):
#         return True
#     else:
#         if text[left] != text[right]:
#             return False
#         left += 1
#         right -= 1
#         is_palindrome_recursive(text, left+1, right-1)

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
