from tkinter import *







def is_winner(board, player):
    if (board[1] == player and board[2] == player and board[3] == player) or \
        (board[4] == player and board[5] == player and board[6] == player) or \
        (board[7] == player and board[8] == player and board[9] == player) or \
        (board[1] == player and board[4] == player and board[7] == player) or \
        (board[2] == player and board[5] == player and board[8] == player) or \
        (board[3] == player and board[6] == player and board[9] == player) or \
        (board[1] == player and board[5] == player and board[9] == player) or \
        (board[3] == player and board[5] == player and board[7] == player):
        return True
    else:
        return False

def is_board_full(board):
    if " " in board:
        return False
    return True






import copy
import random
from math import sqrt, log, inf


def player_turn(board):
    count = 0
    for i in range (1, 10):
        if board[i] == " ":
            count += 1
    if count % 2 == 0:
        return "O"
    else:
        return "X"


def children (board):
    player = player_turn(board)
    children = []
    for i in range (1,10):
        if board[i] == " ":
            new_board = copy.deepcopy(board)
            new_board[i] = player
            children.append(new_board)
    return children



tree = {}

tree["0"] = [[""," "," "," "," "," "," "," "," "," "], None, 0, 1, []]    # représentation, parent, nombre de victoire, nombre de visite, enfants

def is_final_state(leaf):

    board = tree[leaf][0]
    if is_winner(board,"X") or is_winner(board,"O") or is_board_full(board):
        return True
    return False
