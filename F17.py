# F17 - Exit
from functions import *
from F16 import *

def exit(username, store_game, riwayat, kepemilikan):
    print("Exit")
    print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    s = input()
    while not cekExit(s):
        print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
        s = input()
    if (s == "Y") or (s == "y"):
        save(username, store_game, riwayat, kepemilikan)
    return
