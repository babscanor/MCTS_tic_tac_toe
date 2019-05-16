from game import *

import copy
import random
from math import sqrt, log, inf

def string_to_board(noeud):
    board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    i = 1
    while i < len(noeud):
        if i%2 == 1:
            board[int(noeud[i])] = "X"
        elif i%2 == 0:
            board[int(noeud[i])] = "O"
        i += 1
    return board

def print_board(board):
    print("   |   |   ")
    print(" "+board[1]+" | "+board[2]+" | "+board[3])
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" "+board[4]+" | "+board[5]+" | "+board[6])
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" "+board[7]+" | "+board[8]+" | "+board[9])
    print("   |   |   ")


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

def is_final_state(node, tree):

    board = tree[node][0]
    if is_winner(board,"X") or is_winner(board,"O") or is_board_full(board):
        return True
    return False

def is_final_state_2(board):
    if is_winner(board,"X") or is_winner(board,"O") or is_board_full(board):
        return True
    return False


def expansion(root, tree):

    childs = children(tree[root][0])
    for child in childs :
        i = 1
        while tree[root][0][i] == child[i] and i <= 9:
            i += 1
        tree[root + str(i)] = [child, root, 0, 1, 0, []]
        tree[root][5].append(root + str(i))


def selection_node(root, tree):

    while len(tree[root][5]) != 0:
        for child in tree[root][5]:
            tree[child][4] = (tree[child][2]/tree[child][3]) + sqrt((7*log(tree[root][3]))/tree[child][3])
        maximum = max([tree[child][4] for child in tree[root][5]])
        possible_leaf = []
        for child in tree[root][5]:
            if tree[child][4] == maximum:
                possible_leaf.append(child)
        root = possible_leaf[random.randint(0,len(possible_leaf)-1)]

    return root


def empty_places(board):
    count = 0
    for i in range (1,10):
        if board[i] == " ":
            count += 1
    return count

def situation_bizarre(board):
    if (board[5] == "X" and board[6] == "X") or (board[5] == "X" and board[4] == "X") or (board[5] == "X" and board[2] == "X") or(board[5] == "X" and board[8] == "X"):
        return True



def simulation_1(leaf,tree,play):

    new_board = copy.deepcopy(tree[leaf][0])
    empty_places = []
    for i in range (1,10):
        if new_board[i] == " ":
            empty_places.append(i)
    while not is_final_state_2(new_board):
        player = player_turn(new_board)
        indice = random.randint(0, len(empty_places)-1)
        new_board[empty_places[indice]] = player
        del empty_places[indice]
    if is_winner(new_board,"X"):
        if play == "X":
            return 1
        if play == "O":
            return -3
    if is_winner(new_board,"O"):
        if play == "X":
            return -3
        if play == "O":
            return 1
    return 0

def simulation_2(leaf,tree,play):


    new_board = copy.deepcopy(tree[leaf][0])
    empty_places = []
    for i in range (1,10):
        if new_board[i] == " ":
            empty_places.append(i)
    while not is_final_state_2(new_board):
        player = player_turn(new_board)
        indice = random.randint(0, len(empty_places)-1)
        new_board[empty_places[indice]] = player
        del empty_places[indice]
    if is_winner(new_board,"X"):
        if play == "X":
            return 1
        if play == "O":
            return -20
    if is_winner(new_board,"O"):
        if play == "X":
            return -20
        if play == "O":
            return 1
    return 0





def mcts(nombre_iteration, root, player):


    tree = {}
    tree[root] = [string_to_board(root), None, 0, 1, 0, []]


    for i in range (nombre_iteration):          # on répète le même processus

        # selection

        leaf = selection_node(root, tree)
        #print(leaf)
        # expansion

        if not is_final_state(leaf, tree):
            expansion(leaf, tree)
            leaf = tree[leaf][5][random.randint(0, len(tree[leaf][5])-1)]

            # simulation

            if empty_places(tree[leaf][0]) <= 5:
                result = simulation_2(leaf,tree,player)


            else:
                result = simulation_1(leaf, tree, player)
        else :

            if empty_places(tree[leaf][0]) <= 5:
                result = simulation_2(leaf,tree,player)

            else:
                result = simulation_1(leaf, tree, player)

        # backpropagation


        while leaf != root:
            tree[leaf][3] += 1
            tree[leaf][2] += result
            leaf = tree[leaf][1]
        tree[root][3] += 1
        tree[root][2] += result

    # renvoyer le meilleur choix possible

    for child in tree[root][5]:
        tree[child][4] = (tree[child][2]/tree[child][3]) + sqrt((7*log(tree[root][3]))/tree[child][3])
        #print(tree[child])
    maximum = max([tree[child][4] for child in tree[root][5]])
    possible_leaf = []
    for child in tree[root][5]:
        if tree[child][4] == maximum:
            possible_leaf.append(child)
    move = possible_leaf[random.randint(0,len(possible_leaf)-1)]

    return move



root = "O"
board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

#for i in range (10):

   # print(mcts(500000,"05173","X"))




while True:

    print_board(board)

    # Get X input

    '''
    dico_X = {}
    for i in range (10):
        resultat = mcts(100000,root,"X")
        if resultat in dico_X:
            dico_X[resultat] += 1
        else:
            dico_X[resultat] = 1
    maximum_X = max(dico_X.values())
    best_move_X = None
    for key in dico_X.keys():
        if dico_X[key] == maximum_X:
            best_move_X = key

    for child in tree[root][4]:
        print(tree[child])
'''

    choice = input("Choississez un emplacement pour X : ")
    choice = int(choice)

    # Check empty space
    #while board[choice] != " ":
       # print("Sorry that space is not empty")
        #choice = input("Choississez un emplacement pour X : ")
        #choice = int(choice)

    board[choice] = "X"

    root += str(choice)

    # Check for X win
    if is_winner(board, 'X'):
        print_board(board)
        print("X wins! Congratulations!")
        break

    #Check for a tie
    if is_board_full(board):
        print("Tie!")
        break


    # Get AI move

    dico_O = {}
    for i in range (10):
        resultat = mcts(100000,root,"O")
        if resultat in dico_O:
            dico_O[resultat] += 1
        else:
            dico_O[resultat] = 1
    maximum_O = max(dico_O.values())
    best_move_O = None
    for key in dico_O.keys():
        if dico_O[key] == maximum_O:
            best_move_O = key

    board[int(best_move_O[len(best_move_O)-1])] = "O"
    root = best_move_O


    # Check for O win
    if is_winner(board, 'O'):
        print_board(board)
        print("O wins! Congratulations!")
        break

    #Check for a tie
    if is_board_full(board):
        print_board(board)
        print("Tie!")
        break













