# F17 - Exit
from functions import *

def exit():
    print("Exit")
    print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    s = input()

    while not cekExit(s):
        print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
        s = input()
    return