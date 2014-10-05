#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Susan Sim, Jessica Mann and Juntian Wang'
__email__ = "ses@drsusansim.org, jess.mann@mail.utoronto.ca and justinjtwang@gmail.com"

__copyright__ = "2014 Susan Sim, Jessica Mann and Juntian Wang"
__license__ = "MIT License"

__status__ = "Version 2"

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
    legal_letter_grades = ["A+", "A", "A-", "B+", "B", "B-", "FZ"]

    if type(grade) is str:
        # check that the grade is one of the accepted values
        if grade in legal_letter_grades:
            # assign grade to letter_grade
            letter_grade = grade
        else:
            raise ValueError("That's not a valid letter grade.")
    elif type(grade) is int:
        # check that grade is in the accepted range
        # convert the numeric grade to a letter grade
        if grade > 89:
            mark_to_letter = "A+"
        elif 89 >= grade >= 85:
            mark_to_letter = "A"
        elif 84 >= grade >= 80:
            mark_to_letter = "A-"
        elif 79 >= grade >= 77:
            mark_to_letter = "B+"
        elif 76 >= grade >= 73:
            mark_to_letter = "B"
        elif 72 >= grade >= 70:
            mark_to_letter = "B-"
        elif 69 >= grade >= 0:
            mark_to_letter = "FZ"
        else:
            raise ValueError("That's not a valid mark.")
        # assign the value to letter_grade
        letter_grade = mark_to_letter

    # write a long if-statement to convert letter_grade
    # assign the value to gpa
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
        # raise a TypeError exception
        raise TypeError("Invalid type passed as parameter.")
    return gpa


