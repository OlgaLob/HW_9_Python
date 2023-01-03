# Tic Tac Toe game with GUI
# using tkinter
 
# importing all necessary libraries
import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy
 
# переменная для определения очередности
sign = 0
 
# создание пустого поля
global board
board = [[" " for x in range(3)] for y in range(3)]

# определение победителя по правилам игры
  
def winner(b, l):
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l))
 
# Создание текста на кнопках в игре между двумя игроками
def get_text(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    if winner(board, "X"):
        gb.destroy()
        box = messagebox.showinfo("Победитель", "Победил игрок 1")
    elif winner(board, "O"):
        gb.destroy()
        box = messagebox.showinfo("Победитель", "Победил игрок 2")
    elif(isfull()):
        gb.destroy()
        box = messagebox.showinfo("Ничья", "Победила дружба!")
 
# Проверка, нажал игрок кнопку или нет
 
 
def isfree(i, j):
    return board[i][j] == " "
 
# Проверка, пустое поле или нет
 
 
def isfull():
    flag = True
    for i in board:
        if(i.count(' ') > 0):
            flag = False
    return flag
 
# Создание графического интерфейса игровой доски для игры двух игроков
  
def gameboard_pl(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()
 
# Принятие решения о следующем ходе компьютера
 
 
def pc():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if possiblemove == []:
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner)-1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge)-1)
            return edge[move]
 
# Настройка текста на кнопке при игре с компьютером
 
 
def get_text_pc(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Победитель", "Победил игрок")
    elif winner(board, "O"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Победитель", "Победил компьютер")
    elif(isfull()):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Ничья", "Победила дружба!")
    if(x):
        if sign % 2 != 0:
            move = pc()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_pc(move[0], move[1], gb, l1, l2)
 
# Создание интерфейса для игры с компьютером
 
 
def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()
 
# Запуск игры с компьютером
 
 
def withpc(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Игра крестики - нолики")
    l1 = Button(game_board, text="Игрок : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text="Компьютер : O",
                width=12, state=DISABLED)
 
    l2.grid(row=2, column=1)
    gameboard_pc(game_board, l1, l2)
 
# Запуск игры с двумя игроками
 
 
def withplayer(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Игра крестики-нолики")
    l1 = Button(game_board, text="Игрок 1 : X", width=10)
 
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text="Игрок 2 : O",
                width=10, state=DISABLED)
 
    l2.grid(row=2, column=1)
    gameboard_pl(game_board, l1, l2)
 
# главное окно игры
 
 
def play():
    menu = Tk()
    menu.geometry("500x200")
    menu.title("Игра крестики-нолики")
    wpc = partial(withpc, menu)
    wpl = partial(withplayer, menu)
 
    head = Button(menu, text="---Добро пожаловать в игру крестики-нолики---",
                  activeforeground='darkblue',
                  activebackground="white", bg="darkblue",
                  fg="white", width=500, font='summer', bd=5)
 
    B1 = Button(menu, text="Один игрок", command=wpc,
                activeforeground='darkblue',
                activebackground="white", bg="darkblue",
                fg="white", width=500, font='summer', bd=5)
 
    B2 = Button(menu, text="Два игрока", command=wpl, activeforeground='darkblue',
                activebackground="white", bg="darkblue", fg="white",
                width=500, font='summer', bd=5)
 
    B3 = Button(menu, text="Выход", command=menu.quit, activeforeground='darkblue',
                activebackground="white", bg="darkblue", fg="white",
                width=500, font='summer', bd=5)
    head.pack(side='top')
    B1.pack(side='top')
    B2.pack(side='top')
    B3.pack(side='top')
    menu.mainloop()
 
 
# Вызов главного окна
if __name__ == '__main__':
    play()