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

def digit(number, n):
    return int( (number % (10^n) ) / (10 ^ (n-1) ) )

def checksum (upc):
    if type(upc) != int:
        raise TypeError
    if upc < 10^11 | upc >= 10^12:
        raise ValueError

    sumodd = digit(upc, 2) + digit(upc, 4) + digit(upc, 6) + digit(upc, 8) + digit(upc, 10) + digit(upc, 12)
    sumeven = digit(upc, 3) + digit(upc, 5) + digit(upc, 7) + digit(upc, 9) + digit(upc, 11)
    result = 10 - ((sumodd * 3 + sumeven) % 10)
    return upc % 10 == result

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
