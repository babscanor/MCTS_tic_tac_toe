import random

board = [""," "," "," "," "," "," "," "," "," "]


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

def get_computer_move(board,player1,player2):

    # Check for a win
    for i in range(1,10):
        if board[i] == " ":
            board[i] = player1
            if is_winner(board, player1):
                board[i] = " "
                return i
            else:
                board[i] = " "

    # Check for a block
    for i in range(1,10):
        if board[i] == " ":
            board[i] = player2
            if is_winner(board, player2):
                board[i] = " "
                return i
            else:
                board[i] = " "

    while True:
        indice = []
        for i in range (1, len(board)):
            if board[i] == " ":
                indice.append(i)
        return indice[random.randint(0,len(indice)-1)]



while True:

    print_board(board)

    # Get X input
    choice = input("Choississez un emplacement pour X : ")
    choice = int(choice)

    # Check empty space
    while board[choice] != " ":
        print("Sorry that space is not empty")
        choice = input("Choississez un emplacement pour X : ")
        choice = int(choice)

    board[choice] = "X"

    # Check for X win
    if is_winner(board, 'X'):
        print_board(board)
        print("X wins! Congratulations!")
        break

    print_board(board)

    #Check for a tie
    if is_board_full(board):
        print("Tie!")
        break


    board[get_computer_move(board, "O", "X")] = "O"

    # Check for O win
    if is_winner(board, 'O'):
        print_board(board)
        print("O wins! Congratulations!")
        break

    #Check for a tie
    if is_board_full(board):
        print("Tie!")
        break


