#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.

    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """

    letter_grade = ""
    number_grade = 0
    gpa = 0.0

    if type(grade) is str:
        letter_grade = grade
        if letter_grade == "A+":
            gpa = 4.0
        elif letter_grade == "A":
            gpa = 4.0
        elif letter_grade == "A-":
            gpa = 3.7
        elif letter_grade == "B+":
            gpa = 3.3
        elif letter_grade == "B":
            gpa = 3.0
        elif letter_grade == "B-":
            gpa = 2.7
        elif letter_grade == "FZ":
            gpa = 0.0
        else:
            raise ValueError

    elif type(grade) is int:
        number_grade = grade
        if number_grade >89:
            gpa = 4.0
        elif 89 >= number_grade >= 85:
            gpa = 4.0
        elif 84 >= number_grade >= 80:
            gpa = 3.7
        elif 79 >= number_grade >= 77:
            gpa = 3.3
        elif 76 >= number_grade >= 73:
            gpa = 3.0
        elif 72 >= number_grade >= 70:
            gpa = 2.7
        elif 69 >= number_grade >= 0:
            gpa = 0.0
        else:
            raise ValueError

    else:
        # raise a TypeError exception
        raise TypeError("Invalid type passed as parameter")

    return gpa



