from run import *
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
            #print_board(board)
            return 1
        if is_winner(new_board,player) and player == "0":
            #print_board(board)
            return 0
        indice = random.randint(0, len(empty_places)-1)
        new_board[empty_places[indice]] = player
        del empty_places[indice]
    if is_winner(new_board,"X"):
        #print_board(board)
        return 1
    #print_board(board)
    return 0



def mcts(nombre_iteration, root):

    global tree

    for i in range (nombre_iteration):          # on répète le même processus

        # selection

        leaf = selection_node(root)

        # expansion

        expansion(leaf)
        random_child = tree[leaf][4][random.randint(0, len(tree[leaf][4])-1)]

        # simulation

        result = simulation(tree[random_child][0])

        # backpropagation

        while random_child != root:
            tree[random_child][3] += 1
            if result == 1 :
                tree[random_child][2] += 1
            random_child = tree[random_child][1]
        tree[root][3] += 1
        if result == 1 :
            tree[root][2] += 1


    # renvoyer le meilleur choix possible

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

















