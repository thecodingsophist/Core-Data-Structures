#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

# ======================================================
# ORGANIZING DATA
# ======================================================
numbers = ['0','1','2','3','4','5','6','7','8','9']

more_numbers = ['10','11','12','13','14','15','16',
'17', '18', '19','20','21','22','23','24','25','26','27','28',
'29','30','31','32','33','34','35']

key = {'a': 10,
       'b': 11,
       'c': 12,
       'd': 13,
       'e': 14,
       'f': 15,
       'g': 16,
       'h': 17,
       'i': 18,
       'j': 19,
       'k': 20,
       'l': 21,
       'm': 22,
       'n': 23,
       'o': 24,
       'p': 25,
       'q': 26,
       'r': 27,
       's': 28,
       't': 29,
       'u': 30,
       'v': 31,
       'w': 32,
       'x': 33,
       'y': 34,
       'z': 35 }

unkey = dict(zip(numbers+more_numbers, list(string.digits+string.ascii_lowercase)))


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    # DECODE DIGITS FROM BINARY (BASE 2)
    # reverse_digits = reversed(digits)
    # base_ten = 0
    # counter = 0
    # for digit in reverse_digits:
    #     base_ten += int(digit)*(base**counter)
    #     counter += 1
    # # print(base_ten)
    # return base_ten

    # DECODE DIGITS FROM HEXADECIMAL (BASE 16)
    # ======================================================
    # ORGANIZING DATA
    # ======================================================
    # numbers = ['1','2','3','4','5','6','7','8','9']
    # key = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15 }
    # ======================================================
    # DATA SETUP
    # ======================================================
    #
    # # reverse_digits = reversed(digits)
    # base_sixteen = 0
    # counter = 0
    # ======================================================
    # DATA FUNCTION
    # ======================================================
    #
    # for digit in reversed(digits):
    #     # print digit
    #     if digit in numbers:
    #         base_sixteen += int(digit)*(base**counter)
    #         # print(base_sixteen)
    #     elif digit in key:
    #         int_digit = key[digit]
    #         base_sixteen += int(int_digit)*(base**counter)
    #         # print(base_sixteen)
    #     counter += 1
    # # print(base_sixteen)
    # return base_sixteen

    # DECODE DIGITS FROM ANY BASE (2-16)
    # ======================================================
    # DATA SETUP
    # ======================================================
    base_total = 0
    counter = 0
    # ======================================================
    # DATA FUNCTION
    # ======================================================
    for digit in reversed(digits):
        # print digit
        if digit in numbers:
            base_total += int(digit)*(base**counter)
            # print(base_sixteen)
        elif digit in key:
            int_digit = key[digit]
            base_total += int(int_digit)*(base**counter)
            # print(base_sixteen)
        counter += 1
    # print(base_sixteen)
    return base_total


def encode(number, base):

    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    # Encode number in binary (base 2)
    # IDEA: while number(dividend) > 0, loop through: divide number(dividend) by base, add remainder to A_string, return reversed A_string
    # A_string = ""
    # dividend = number
    # while dividend > 0:
    #     A_string += str(dividend%base)
    #     dividend = dividend//base
    # print(A_string[::-1])
    # return A_string[::-1]

    # Encode number in hexadecimal (base 16)
    # IDEA: same as converting to binary, but use global dictionary to change quotient to hexadecimal
    A_string = ""
    dividend = number
    while dividend > 0:
        # change quotient to hexadecimal
        quotient = dividend//base
        print("quotient=" + str(quotient))
        hexidecimal = unkey[str(dividend%base)]
        print("hexidecimal=" + hexidecimal)
        A_string += hexidecimal
        # find next dividend
        dividend = dividend//base
        print("dividend=" + str(dividend))
    print(A_string[::-1])
    return A_string[::-1]

    # TODO: Encode number in any base (2 up to 36)
    # ...


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    return encode(digits, base2)
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = int(args[0])
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')



if __name__ == '__main__':
    main()
