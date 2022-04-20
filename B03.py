# B03 - Game Tic-Tac-Toe
from functions import *

def B03():
    print("Tic-Tac-Toe\n")
    P = [["#" for j in range (3)] for i in range (3)]
    print("Keterangan: ")
    print("# = kosong")
    print("X = Pemain 1")
    print("O = Pemain 2")
    printBoard(P)

    t = 1
    while not cekFull(P):
        if (t % 2 != 0):
            print("Giliran player pertama (X):")
            P = play(P,"X")
        else: #(t % 2 != 0)
            print("Giliran player kedua (O): ")
            play(P,"O")
        t = t + 1
        printBoard(P)
        if cekWin(P,"X"):
            print("Player pertama (X) menang")
            break
        elif cekWin(P,"O"):
            print("Player kedua (O) menang")
            break
    if not (cekWin(P,"X") or cekWin(P,"O")):
        print("Seri")
    return