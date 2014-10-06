#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Susan Sim, Jessica Mann and Juntian Wang'
__email__ = "ses@drsusansim.org, jess.mann@mail.utoronto.ca and justinjtwang@gmail.com"

__copyright__ = "2014 Susan Sim, Jessica Mann and Juntian Wang"
__license__ = "MIT License"

__status__ = "Final version"


def checksum(upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a string
        ValueError if string is the wrong length (with error string stating how many digits are over or under)
    """

    # check type of input
    # raise TypeError if not string
    if type(upc) != str:
        raise TypeError

    # check length of string
    # raise ValueError if not 12 (with error string stating how many digits are over or under)
    if len(str(upc)) > 12:
        raise ValueError("This UPC code is too long by " + str((len(str(upc))) - 12) + " characters.")
    if len(str(upc)) < 12:
        raise ValueError("This UPC code is too short by " + str(12 - (len(str(upc)))) + " characters.")

    # convert string to two arrays needed for the checksum calculation: odd and even numbers
    odd_digit_numbers = upc[0::2]
    even_digit_numbers = upc[1::2]

    # calculate the checksum using the first 11 digits provided
    # create a variable to hold the odd and even number addition and multiplication
    sum_of_odd_and_even = 0

    # do the odd and even digit addition and multiplication from arrays created
    for digit in odd_digit_numbers:
        sum_of_odd_and_even += 3 * int(digit)
    for digit in even_digit_numbers:
        sum_of_odd_and_even += int(digit)

    # from modulo 10 of the result, use the modulo or 0 as the final checksum calculation
    calculated_checksum = (10 - ((sum_of_odd_and_even - int(upc[11])) % 10)) % 10

    # check the calculated against the the twelfth digit i.e. the checksum itself
    # return True if they are equal, False otherwise
    return int(upc[11]) == calculated_checksum
