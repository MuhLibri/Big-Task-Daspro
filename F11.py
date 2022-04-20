# F11 - Mencari Game di Toko dari ID, Nama Game, Harga, Kategori dan Tahun Rilis
from functions import *

def storeGameSearch():
    longest_name = lenMax(1)
    longest_genre = lenMax(2)
    longest_price = lenMax(4)
    print("Cari Game di Toko")
    GameID = input("Masukkan ID Game: ")
    GameName = input("Masukkan Nama Game: ")
    Price = input("Masukkan Harga Game: ")
    Genre = input("Masukkan Kategori Game: ")
    Year = input("Masukkan Tahun Rilis Game: ")
    game_info = open("store_game.csv",'r')
    search_game = game_info.readline()
    search_game = game_info.readline()
    num = 1

    print("Daftar game pada toko yang memenuhi kriteria: ")
    while (search_game != ""):
        if ((GameID == parse(search_game)[0]) or (GameID == "")) and ((GameName == parse(search_game)[1]) or (GameName == "")) and ((Genre == parse(search_game)[2]) or (Genre == "")) and ((Year == parse(search_game)[3]) or (Year == "")) and ((Price == parse(search_game)[4]) or (Price == "")):
            cleanPrintStore(num,parse(search_game)[0],parse(search_game)[1],parse(search_game)[2],parse(search_game)[3],parse(search_game)[4],parse(search_game)[5],longest_name,longest_genre,longest_price)
            num = num + 1
        search_game = game_info.readline()
    if (num == 1):
        print("Tidak ada game pada toko memenuhi kriteria")
    game_info.close()
    return
