#!/usr/bin/env python3

comparator = {}
comparator[("Scissors", "Scissors")] = 0
comparator[("Scissors", "Paper")] = 1
comparator[("Scissors", "Rock")] = 2
comparator[("Paper", "Scissors")] = 2
comparator[("Paper", "Paper")] = 0
comparator[("Paper", "Rock")] = 1
comparator[("Rock", "Scissors")] = 1
comparator[("Rock", "Paper")] = 2
comparator[("Rock", "Rock")] = 0

def decide_rps(player1, player2):
    return comparator[(player1, player2)]


