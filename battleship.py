#!/usr/bin/env python
# encoding=utf8
from __future__ import print_function
import numpy as np
import string

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Array KEY
# 0 = nothing
# 1 = ship (undamaged)
# 2 = miss
# 3 = hit

# init players
p1 = {}
p2 = {}
whosturn = "p1"

bwidth = 10
bheight = 10

# init player boards
p1b = np.zeros((bheight,bwidth), dtype=int)
p2b = np.zeros((bheight,bwidth), dtype=int)

# init player guesses
p1g = np.zeros((bheight,bwidth), dtype=int)
p2g = np.zeros((bheight,bwidth), dtype=int)


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
            print(" %s " % render_coord(board[y,x]), end="")
        # print(string.uppercase[y])
        print()
    print(" ", end="")
    # for n in range(cols):
    #     print(" %s " % n, end="")
    print()

# Public: Renders a unicode character given the value n
def render_coord(n):
    switcher = {
        1: "S", # undamaged ship
        2: "o", # missed shot
        3: "X"  # hit ship
    }
    return switcher.get(n, ".") # default to empty space

def render_player (player):
    print("        " + player['name'] + " Guesses")
    render_board(player['guesses'])
    print("\n        " + player['name'] + " Ships")
    render_board(player['ships'])

def guess (board, col, row):
    if (board[row,col] == 1):
        board.itemset((row,col), 3)
        return True
    if (board[row,col] == 0):
        board.itemset((row,col), 2)
        return False
    else:
        return False

def main ():
    while True:
        print("Input in the format of 'X Y [v]'")
        action = raw_input("Coordinates: ").split()
        if validate_input(action):
            if place_ship(p1b, int(action[0]), int(action[1]), 3, action[2]):
                render_player(p1)
            else:
                print("Doesn't fit there. Try again.")

    # track who's turn it is
    # get players names
    # generate unique game ID + url

def validate_input (action):
    try:
        isinstance(action[0], str)
    except:
        return False
    else:
        if action[0] == "q":
            exit()
        if len(action) < 3:
            action.append("h")
    try:
        isinstance(int(action[0]), int)
        isinstance(int(action[1]), int)
    except:
        print("Invalid input. Try again.")
        return False
    else:
        return True

def place_ship (board, col, row, size, orientation):
    if orientation == "v" and (size + row) > 10:
        return False
    if orientation == "h" and (size + col) > 10:
        return False
    y = row - 1
    x = col - 1

    for i in range(size):
        if orientation == "h" and board[y,x+i] != 0:
            return False
        if orientation == "v" and board[y+i,x] != 0:
            return False

    for i in range(size):
        if orientation == "h":
            board.itemset((y, x+i), 1)
        else:
            board.itemset((y+i, x), 1)
    return True

    # logic check for spillover
    # logic check for overlap with existing ships

# p1b.itemset((3,5), 1)
# p1b.itemset((4,5), 1)
# p1b.itemset((9,2), 2)
# p1b.itemset((2,7), 3)

main()
