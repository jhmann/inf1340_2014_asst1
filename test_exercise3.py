#!/usr/bin/env python3

""" Module to test exercise3.py """

__author__ = 'Susan Sim, Jessica Mann and Juntian Wang'
__email__ = "ses@drsusansim.org, jess.mann@mail.utoronto.ca and justinjtwang@gmail.com"

__copyright__ = "2014 Susan Sim, Jessica Mann and Juntian Wang"
__license__ = "MIT License"

__status__ = "Final version"

# imports one per line

import pytest
from exercise3 import decide_rps


def test_checksum():
    """
    Inputs that are valid
    """
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Rock", "Scissors") == 1
    assert decide_rps("Scissors", "Paper") == 1
    assert decide_rps("Scissors", "Rock") == 2
    assert decide_rps("Paper", "Scissors") == 2
    assert decide_rps("Paper", "Paper") == 0
    assert decide_rps("Paper", "Rock") == 1
    assert decide_rps("Rock", "Rock") == 0


def test_invalid_input():
    """
    Inputs that are invalid
    """
    with pytest.raises(ValueError):
        assert decide_rps("Spock", "Lizard")

    with pytest.raises(ValueError):
        assert decide_rps("Spock", "Scissors")

    with pytest.raises(ValueError):
        assert decide_rps("Rock", "Lizard")

    with pytest.raises(ValueError):
        assert decide_rps(1, 5)                                             # testing integers

    with pytest.raises(ValueError):
        assert decide_rps(5.0, 3.141)                                       # testing floats

    with pytest.raises(ValueError):
        assert decide_rps(False, "Different data type")                     # testing differing data types