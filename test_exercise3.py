#!/usr/bin/env python3

import pytest
from exercise3 import decide_rps


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Rock", "Scissors") == 1
    # other tests

def test_invalid_input():
    with pytest.raises(ValueError):
        assert decide_rps("Spock", "Lizard")
        assert decide_rps("Spock", "Scissors")
        assert decide_rps("Rock", "Lizard")

