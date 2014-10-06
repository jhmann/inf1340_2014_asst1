#!/usr/bin/env python3

""" Module to test exercise2.py """

__author__ = 'Susan Sim, Jessica Mann and Juntian Wang'
__email__ = "ses@drsusansim.org, jess.mann@mail.utoronto.ca and justinjtwang@gmail.com"

__copyright__ = "2014 Susan Sim, Jessica Mann and Juntian Wang"
__license__ = "MIT License"

__status__ = "Final version"

# imports one per line
import pytest
from exercise2 import checksum


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert checksum("786936224306") is True
    assert checksum("085392132225") is True
    assert checksum("717951000841") is False
    assert checksum("158635895321") is True   # added test
    assert checksum("123456789012") is True  # added test
    assert checksum("000000000000") is True  # added test
    assert checksum("737373737373") is False  # added test
    assert checksum("888888888888") is False  # added test


def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with pytest.raises(TypeError):
        checksum(1.0)

    with pytest.raises(TypeError):
        checksum(786936224306)

    with pytest.raises(ValueError):
        checksum("this is so not a checksum")   # added test: a string

    with pytest.raises(TypeError):
        checksum((1, 2, 3, "try-a-tuple"))      # added test: a tuple

    with pytest.raises(TypeError):
        checksum(False)                         # added test: a boolean

    with pytest.raises(ValueError):
        checksum("1")

    with pytest.raises(ValueError):
        checksum("1234567890")

    with pytest.raises(ValueError):
        checksum("45890790580938209840986098")  # added test: too long

    with pytest.raises(TypeError):
        checksum(5*8)                           # added test: too short (and also a formula)
