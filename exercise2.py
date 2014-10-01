#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

def checksum (upc):
    if type(upc) != str:
        raise TypeError
    if len(upc) != 12:
        raise ValueError

    odd_digits_numbers = upc[0::2]
    even_digits_numbers = upc[1::2]

    sum = 0
    for digit in odd_digits_numbers:
        sum += 3 * int(digit)
    for digit in even_digits_numbers:
        sum += int(digit)
    result = 10 - ((sum - int(upc[11])) % 10)
    return int(upc[11]) == result

    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a strong
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    # check type of input
    # raise TypeError if not string

    # check length of string
    # raise ValueError if not 12

    # convert string to array
    # hint: use the list function

    # generate checksum using the first 11 digits provided
    # check against the the twelfth digit

    # return True if they are equal, False otherwise
