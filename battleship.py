#!/usr/bin/env python
from __future__ import print_function
import numpy as np
import string

# Array KEY
# 0 = nothing
# 1 = ship (undamaged)
# 2 = miss
# 3 = hit

# init players
p1 = {}
p2 = {}

# init player boards
p1b = np.zeros((10,10), dtype=int)
p2b = np.zeros((10,10), dtype=int)

# init player guesses
p1g = np.zeros((10,10), dtype=int)
p2g = np.zeros((10,10), dtype=int)


p1['ships'] = p1b
p1['guesses'] = p1g
p1['name'] = "Player 1"

p2['ships'] = p2b
p2['guesses'] = p2g
p2['name'] = "Player 2"

def render_board (board):
    rows = board.shape[0]
    cols = board.shape[1]

    print(" ", end="")
    for n in range(cols):
        print(" %s " % n, end="")
    print()
    for y in range(rows):
        print(string.uppercase[y], end="")
        for x in range(cols):
            print(" . ", end="")
        print(string.uppercase[y])
    print(" ", end="")
    for n in range(cols):
        print(" %s " % n, end="")
    print()

def render_player (player):
    print("        " + player['name'] + " Guesses")
    render_board(player['guesses'])
    print("\n        " + player['name'] + " Ships")
    render_board(player['ships'])

def check (board, row, col):
    if (board[row,col] == 1):
        board.itemset((row,col), 3)
        return "hit"
    if (board[row,col] == 0):
        board.itemset((row,col), 2)
        return "miss"
    else:
        return "invalid guess"

def main ():
    # track who's turn it is
    # get players names
    # generate unique game ID + url
    #

def place_ship (board, row, col, size, orientation):
    # logic check for spillover
    # logic check for overlap with existing ships

render_player(p1)
print()
render_player(p2)
