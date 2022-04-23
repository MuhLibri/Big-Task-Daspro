# F10 - Mencari Game yang dimiliki dari ID dan tahun rilis
from functions import *
from F09 import *

def ownedIDYR(username):
    longest_name = lenMax(1)
    longest_genre = lenMax(2)
    print("Cari Game yang dimiliki")
    ID = input("Masukkan ID Game: ")
    Year = input("Masukkan Tahun Rilis Game: ")
    game_info = open("store_game.csv",'r')
    search_game = game_info.readline()
    num = 1
    print("Daftar game pada inventory yang memenuhi kriteria: ")
    while (search_game != ""):
        if cekOwnedGame(parse(search_game)[0],username):
            if ((ID == parse(search_game)[0]) or (ID == "")) and ((Year == parse(search_game)[3]) or (Year == "")):
                tampilkan_game_dimiliki(num,parse(search_game)[0],parse(search_game)[1],parse(search_game)[2],parse(search_game)[3],parse(search_game)[4],longest_name,longest_genre)
                num = num + 1
        search_game = game_info.readline()
    if (num == 1):
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
    game_info.close()
    return
