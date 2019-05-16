from tkinter import *
import copy
import random
from math import sqrt, log, inf
from game import *
from MCTS import *


root = "0"

def postobutton(couple):
    compteur=1
    for j in [100+k*100 for k in range(3)]:
        for i in [100+k*100 for k in range(3)]:
            if i<=couple[0]<i+100 and j<=couple[1]<j+100 :
                return compteur
            compteur+=1

def move_manual1():
    global choice
    if board[1]==" " and board.count("X")==board.count("O"):
        board[1]="X"
        but0["text"]=board[1]
        choice=postobutton((fenetre.winfo_pointerx()-fenetre.winfo_rootx(),fenetre.winfo_pointery()-fenetre.winfo_rooty()))
        ai_move()
def move_manual2():
    global choice
    if board[2]==" " and board.count("X")==board.count("O"):
        board[2]="X"
        but1["text"]=board[2]
        choice=postobutton((fenetre.winfo_pointerx()-fenetre.winfo_rootx(),fenetre.winfo_pointery()-fenetre.winfo_rooty()))
        ai_move()
def move_manual3():
    global choice
    if board[3]==" " and board.count("X")==board.count("O"):
        board[3]="X"
        but2["text"]=board[3]
        choice=postobutton((fenetre.winfo_pointerx()-fenetre.winfo_rootx(),fenetre.winfo_pointery()-fenetre.winfo_rooty()))
        ai_move()
def move_manual4():
    global choice
    if board[4]==" " and board.count("X")==board.count("O"):
        board[4]="X"
        but3["text"]=board[4]
        choice=postobutton((fenetre.winfo_pointerx()-fenetre.winfo_rootx(),fenetre.winfo_pointery()-fenetre.winfo_rooty()))
        print(choice)
        ai_move()
def move_manual5():
    global choice
    if board[5]==" " and board.count("X")==board.count("O"):
        board[5]="X"
        but4["text"]=board[5]
        choice=postobutton((fenetre.winfo_pointerx()-fenetre.winfo_rootx(),fenetre.winfo_pointery()-fenetre.winfo_rooty()))
        ai_move()
def move_manual6():
    global choice
    if board[6]==" " and board.count("X")==board.count("O"):
        board[6]="X"
        but5["text"]=board[6]
        choice=postobutton((fenetre.winfo_pointerx()-fenetre.winfo_rootx(),fenetre.winfo_pointery()-fenetre.winfo_rooty()))
        ai_move()
def move_manual7():
    global choice
    if board[7]==" " and board.count("X")==board.count("O"):
        board[7]="X"
        but6["text"]=board[7]
        choice=postobutton((fenetre.winfo_pointerx()-fenetre.winfo_rootx(),fenetre.winfo_pointery()-fenetre.winfo_rooty()))
        ai_move()
def move_manual8():
    global choice
    if board[8]==" " and board.count("X")==board.count("O"):
        board[8]="X"
        but7["text"]=board[8]
        choice=postobutton((fenetre.winfo_pointerx()-fenetre.winfo_rootx(),fenetre.winfo_pointery()-fenetre.winfo_rooty()))
        ai_move()
def move_manual9():
    global choice
    if board[9]==" " and board.count("X")==board.count("O"):
        board[9]="X"
        but8["text"]=board[9]
        choice=postobutton((fenetre.winfo_pointerx()-fenetre.winfo_rootx(),fenetre.winfo_pointery()-fenetre.winfo_rooty()))
        ai_move()



board = [""," "," "," "," "," "," "," "," "," "]

fenetre=Tk()
fenetre.title('Tic_Tac_Toe')
fenetre.iconbitmap("logomorpion.png")
fenetre.geometry('500x500')
titre=Label(fenetre,text="Tic tac toe", font=('Times New Roman',30,'bold') )
titre.pack(side="top")

consigne = Label(text="Choississez un emplacement pour X  ", font=("Times New Roman",15 ,'bold'))
consigne.pack(side="top")

but0=Button(fenetre,padx=10,pady=10,bg='grey', bd=5, text=board[1],command=move_manual1, font=('Times New Roman',50,'bold'))
but0.place(x=100,y=100,width=100,height=100)
but1=Button(fenetre,padx=10,pady=10,bg='grey', bd=5, text=board[2],command=move_manual2, font=('Times New Roman',50,'bold'))
but1.place(x=200,y=100,width=100,height=100)
but2=Button(fenetre,padx=10,pady=10,bg='grey', bd=5, text=board[3],command=move_manual3, font=('Times New Roman',50,'bold'))
but2.place(x=300,y=100,width=100,height=100)
but3=Button(fenetre,padx=10,pady=10,bg='grey', bd=5, text=board[4] ,command=move_manual4, font=('Times New Roman',50,'bold'))
but3.place(x=100,y=200,width=100,height=100)
but4=Button(fenetre,padx=10,pady=10,bg='grey', bd=5, text=board[5],command=move_manual5, font=('Times New Roman',50,'bold'))
but4.place(x=200,y=200,width=100,height=100)
but5=Button(fenetre,padx=10,pady=10,bg='grey', bd=5, text=board[6],command=move_manual6, font=('Times New Roman',50,'bold'))
but5.place(x=300,y=200,width=100,height=100)
but6=Button(fenetre,padx=10,pady=10,bg='grey', bd=5, text=board[7],command=move_manual7, font=('Times New Roman',50,'bold'))
but6.place(x=100,y=300,width=100,height=100)
but7=Button(fenetre,padx=10,pady=10,bg='grey', bd=5, text=board[8],command=move_manual8, font=('Times New Roman',50,'bold'))
but7.place(x=200,y=300,width=100,height=100)
but8=Button(fenetre,padx=10,pady=10,bg='grey', bd=5, text=board[9],command=move_manual9, font=('Times New Roman',50,'bold'))
but8.place(x=300,y=300,width=100,height=100)



def update_fenetre():
    but0["text"]=board[1]
    but1["text"]=board[2]
    but2["text"]=board[3]
    but3["text"]=board[4]
    but4["text"]=board[5]
    but5["text"]=board[6]
    but6["text"]=board[7]
    but7["text"]=board[8]
    but8["text"]=board[9]



board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

root = "0"

def ai_move():
    global root
    global choice
    root+=str(choice)
    # Check for X win
    if is_winner(board, 'X'):
        winx=Label(fenetre, text="X wins! Congratulations!")
        winx.pack(side="bottom")
        update_fenetre()

    #Check for a tie
    if is_board_full(board):
        tie=Label(fenetre, text="It's a tie!")
        tie.pack(side="bottom")
        update_fenetre()

    # Get AI move

    dico_O = {}
    for i in range (10):
        resultat = mcts(10000,root,"O")
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
    update_fenetre()

    # Check for O win
    if is_winner(board, 'O'):
        wino=Label(fenetre, text="O wins! Congratulations!")
        wino.pack(side="bottom")
        update_fenetre()

    #Check for a tie
    if is_board_full(board):
        tie=Label(fenetre, text="It's a tie!")
        tie.pack(side="bottom")
        update_fenetre()

fenetre.mainloop()
























