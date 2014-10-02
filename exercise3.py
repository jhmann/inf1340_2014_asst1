#!/usr/bin/env python3

"""
    Return the result of a rock, paper, scissors game

    Assignment 1, Exercise 3, INF1340 Fall 2014
"""

__author__ = "Jessica Mann and Juntian Wang"
__email__ = "jess.mann@mail.utoronto.ca and justinjtwang@gmail.com"

__copyright__ = "2014 Jessica Mann and Juntian Wang"
__license__ = "MIT License"

__status__ = "Version 2"


# create the variable "game_rules" as an empty dictionary to hold the rules for the game
# created & populated outside the function for efficiency: create and populate once, not every time the function runs
game_rules = {}

# add elements to the data dictionary game_rules
# each line adds a key-value pair
# each key is player1's parameter, player 2's parameter
# each value is 0 for tie, 1 if player1 wins, 2 if player2 wins
game_rules[("Scissors", "Scissors")] = 0
game_rules[("Scissors", "Paper")] = 1
game_rules[("Scissors", "Rock")] = 2
game_rules[("Paper", "Scissors")] = 2
game_rules[("Paper", "Paper")] = 0
game_rules[("Paper", "Rock")] = 1
game_rules[("Rock", "Scissors")] = 1
game_rules[("Rock", "Paper")] = 2
game_rules[("Rock", "Rock")] = 0


#create a function called decide_rps
def decide_rps(player1, player2):
    """(string, string) -> int
    Return the key for value inputs player1 and player2 as contained in game_rules
    Assumes only valid inputs of Scissors, Paper or Rock
    >>> game_rules[("Scissors", "Scissors")]
    0
    """
    try:
        return game_rules[(player1, player2)]
    except KeyError:
        raise ValueError
