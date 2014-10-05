#!/usr/bin/env python3

""" Module to test exercise2.py """

__author__ = 'Susan Sim, Jessica Mann and Juntian Wang'
__email__ = "ses@drsusansim.org, jess.mann@mail.utoronto.ca and justinjtwang@gmail.com"

__copyright__ = "2014 Susan Sim, Jessica Mann and Juntian Wang"
__license__ = "MIT License"

__status__ = "Version 1"

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
        checksum(786936224306)
        checksum("this is so not a checksum")   # added test: a string
        checksum((1, 2, 3, "try-a-tuple"))      # added test: a tuple
        checksum(False)                         # added test: a boolean

    with pytest.raises(ValueError):
        checksum("1")
        checksum("1234567890")
        checksum("45890790580938209840986098")  # added test: too long
        checksum(5*8)                           # added test: too short (and also a formula)


"""Why won't this work?
    #testing value error plus messages
    with pytest.raises(ValueError):
        checksum(394069705494085906809780)
        assert "This UPC code is too long by 12 characters." in str(excinfo.value)

    with pytest.raises(ValueError, "This UPC code is too short by 11 characters."):
        checksum(5)

    with pytest.raises(ValueError, "This UPC code is too short by 7 characters."):
        checksum(63878)

    with pytest.raises(ValueError, "This UPC code is too long by 62 characters."):
        checksum(17683948978745905483694836093860959545345634536574574764346376343469836487)
"""