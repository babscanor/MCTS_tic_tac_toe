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

def expansion(parent):

    global tree


    childs = children(tree[parent][0])
    for child in childs :
        i = 1
        while tree[parent][0][i] == child[i] and i <= 9:
            i += 1
        tree[parent+str(i)] = [child, parent, 0, 1, []]
        tree[parent][4].append(parent+str(i))



def selection_node(root):

    global tree


    while len(tree[root][4]) != 0:
        max = -inf
        for child in tree[root][4]:
            uct_value_child = (tree[child][2]/tree[child][3]) + sqrt((2*log(tree[root][3]))/tree[child][3])
            if uct_value_child > max:
                max = uct_value_child
        possible_leaf = []
        for child in tree[root][4]:
            uct_value_child = (tree[child][2]/tree[child][3]) + sqrt((2*log(tree[root][3]))/tree[child][3])
            if uct_value_child == max:
                possible_leaf.append(child)
        root = possible_leaf[random.randint(0, len(possible_leaf)-1)]
    return root



def simulation (board):

    global tree


    new_board = copy.deepcopy(board)
    empty_places = []
    for i in range (1,10):
        if new_board[i] == " ":
            empty_places.append(i)
    while not is_board_full(new_board):
        player = player_turn(new_board)
        if is_winner(new_board,player) and player == "X":
            return 3
        if is_winner(new_board,player) and player == "0":
            return -3
        indice = random.randint(0, len(empty_places)-1)
        new_board[empty_places[indice]] = player
        del empty_places[indice]
    if is_winner(new_board,"X"):
        return 3
    if is_winner(new_board,"O"):
        return -3
    return 0



def mcts(nombre_iteration, root, player):

    global tree

    for i in range (nombre_iteration):          # on répète le même processus

        # selection

        leaf = selection_node(root)

        # expansion

        if not is_final_state(leaf):
            expansion(leaf)
            leaf = tree[leaf][4][random.randint(0, len(tree[leaf][4])-1)]

            # simulation

            result = simulation(tree[leaf][0])

        else :
            result = simulation(tree[leaf][0])

        # backpropagation

        while leaf != root:
            tree[leaf][3] += 1
            tree[leaf][2] += result
            leaf = tree[leaf][1]
        tree[root][3] += 1
        tree[root][2] += result


    # renvoyer le meilleur choix possible

    if player == "X":
        max = -inf
        for child in tree[root][4]:
            uct_value_child = (tree[child][2]/tree[child][3]) + sqrt((2*log(tree[root][3]))/tree[child][3])
            if uct_value_child > max:
                max = uct_value_child
        possible_leaf = []
        for child in tree[root][4]:
            uct_value_child = (tree[child][2]/tree[child][3]) + sqrt((2*log(tree[root][3]))/tree[child][3])
            if uct_value_child == max:
                possible_leaf.append(child)
        return possible_leaf[random.randint(0, len(possible_leaf)-1)]

    if player == "O":
        min = inf
        for child in tree[root][4]:
            uct_value_child = (tree[child][2]/tree[child][3]) + sqrt((2*log(tree[root][3]))/tree[child][3])
            if uct_value_child < min:
                min = uct_value_child
        possible_leaf = []
        for child in tree[root][4]:
            uct_value_child = (tree[child][2]/tree[child][3]) + sqrt((2*log(tree[root][3]))/tree[child][3])
            if uct_value_child == min:
                possible_leaf.append(child)
        return possible_leaf[random.randint(0, len(possible_leaf)-1)]



root = "0"

board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]


# while True:
#
#
#     print_board(board)
#
#     # Get X input
#
#     best_move_X = mcts(10000,root,"X")
#
#     choice = input("Choississez un emplacement pour X (le meilleur étant "+best_move_X[len(best_move_X)-1]+") :")
#     choice = int(choice)
#
#     # Check empty space
#     while board[choice] != " ":
#         print("Sorry that space is not empty")
#         choice = input("Choississez un emplacement pour X : ")
#         choice = int(choice)
#
#     board[choice] = "X"
#
#     root += str(choice)
#     # Check for X win
#     if is_winner(board, 'X'):
#         print_board(board)
#         print("X wins! Congratulations!")
#         break
#
#     #Check for a tie
#     if is_board_full(board):
#         print("Tie!")
#         break
#
#
#     # Get AI move
#
#
#     best_move_O = mcts(10000,root,"O")
#     board[int(best_move_O[len(best_move_O)-1])] = "O"
#     root = best_move_O
#
#
#     # Check for O win
#     if is_winner(board, 'O'):
#         print_board(board)
#         print("O wins! Congratulations!")
#         break
#
#     #Check for a tie
#     if is_board_full(board):
#         print("Tie!")
#         break
#


















