#!/usr/bin/env python3

"""
    Return the result of a rock, paper, scissors game

    Assignment 1, Exercise 3, INF1340 Fall 2014
"""

__author__ = "Jessica Mann and Juntian Wang"
__email__ = "jess.mann@mail.utoronto.ca and justinjtwang@gmail.com"

__copyright__ = "2014 Jessica Mann and Juntian Wang"
__license__ = "MIT License"

__status__ = "Final version"


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
    """
    Returns the winner of a Rock, Paper, Scissors game.

    :param:
        player1 (string) and player2 (string): player entries
            Accepted entries are "Rock", "Paper" or "Scissors"

    :return:
        int: player1 wins, player2 wins, or tie
            tie = 0
            player1 wins = 1
            player2 wins = 2

    :raises:
        ValueError if parameter is not a valid entry as noted above
    """

    # attempt to pass the parameters as game_rules dictionary keys and return the appropriate dictionary value
    try:
        return game_rules[(player1, player2)]

    # but if a key error is encountered above, raise a value error (Since returning a value or type error difference
    # wasn't specified in this exercise, passing a single error message is more efficient.)
    except KeyError:
        raise ValueError('These are not valid values. Values must be two of "Rock","Scissors", or "Paper".')
