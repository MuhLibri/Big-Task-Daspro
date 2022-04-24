import datetime
from functions import *

def cek_file_user(username, indeks_kolom): #Fungsi untuk mencari data di user.csv berdasarkan username dan mereturn data berdasarkan indeks_kolom
        file_user = open('data_login.csv', 'r')  #indeks_kolom; saldo = 5, user_id = 0
        read_file = file_user.readline()
        while (read_file != ""):
            if (username == parse(read_file)[2]):
                file_user.close()
                return parse(read_file)[indeks_kolom]
            read_file = file_user.readline()

def cek_kepemilikan(game_id, username): #Fungsi untuk mengecek apakah user sudah memiliki game tersebut
        file_kepemilikan = open('kepemilikan.csv', 'r')
        read_file = file_kepemilikan.readline()
        userid = cek_file_user(username, 0)
        while (read_file != ""):
            if (game_id == parse(read_file)[0]) and (userid == parse(read_file)[1]):
                file_kepemilikan.close()
                return True
            read_file = file_kepemilikan.readline()
        file_kepemilikan.close()
        return False
        
def cek_file_game(game_id, indeks_kolom):#Fungsi untuk mencari data di game.csv berdasarkan game_id dan mereturn data berdasarkan indeks_kolom
        file_game = open('store_game.csv', 'r') #indeks_kolom; nama = 1, harga = 4 , stok = 5
        read_file = file_game.readline()
        while (read_file != ""):
            if (game_id == parse(read_file)[0]):
                file_game.close()
                return parse(read_file)[indeks_kolom]
            read_file = file_game.readline()

def newStringRiwayat(username,game_id): #Fungsi untuk menambah string baru pada file riwayat.csv
    new_riwayat = cek_file_user(username, 0)  + ';' + game_id + ';' + cek_file_game(game_id, 1) + ';' + cek_file_game(game_id, 4) + ';' + str(datetime.datetime.now().year)
    new_string = ""
    file_riwayat = open("riwayat.csv",'r')
    read_file = file_riwayat.readline()
    while (read_file != ""):
        new_string = new_string + read_file
        read_file = file_riwayat.readline()
    new_string = new_string + "\n" + new_riwayat
    file_riwayat.close()
    return new_string

def writeRiwayat(game_id):#Fungsi untuk menulis string baru pada file riwayat.csv
    new_data = newStringRiwayat(game_id)
    file_riwayat = open("riwayat.csv",'w')
    write_riwayat = file_riwayat.write(new_data)
    file_riwayat.close()
    return write_riwayat

def newStringKepemilikan(username,game_id): #Fungsi untuk menambah string baru pada file kepemilikan.csv
    new_kepemilikan = game_id + ';' + cek_file_user(username, 0)
    new_string = ""
    file_kepemilikan = open("kepemilikan.csv",'r')
    read_file = file_kepemilikan.readline()
    while (read_file != ""):
        new_string = new_string + read_file
        read_file = file_kepemilikan.readline()
    new_string = new_string + "\n" + new_kepemilikan
    file_kepemilikan.close()
    return new_string

def writeKepemilikan(game_id): #Fungsi untuk menulis string baru pada file kepemilikan.csv
    new_data = newStringKepemilikan(game_id)
    file_kepemilikan = open("kepemilikan.csv",'w')
    write_kepemilikan = file_kepemilikan.write(new_data)
    file_kepemilikan.close()
    return write_kepemilikan

def pengurangan_saldo(username, game_id, matriks_csv): #Prosedur topup saldo user
    indeks = find_indeks(matriks_csv, username, 2)
    matriks_csv[indeks][5] = str(int(matriks_csv[indeks][5]) - int(cek_file_game(game_id, 4))) #Assign saldo baru ke saldo lama (hanya dalam memori) sebelum disave
    print(f"Saldo menjadi {(matriks_csv[indeks][5])}.")

def pengurangan_stok(game_id, matriks_csv): #Prosedur pengurangan stok game
    indeks = find_indeks(matriks_csv, game_id, 0)#
    matriks_csv[indeks][5] = str(int(matriks_csv[indeks][5]) - 1) #Assign stok baru ke stok lama (hanya dalam memori) sebelum disave
    print(f"Stok menjadi {(matriks_csv[indeks][5])}.")

username = "haqufa"

def buyGame(): #Fungsi utama
    game_id = input("Masukan game id : ")
    if not (cek_kepemilikan(game_id, username)):
        userid = cek_file_user(username, 0)
        if int(cek_file_user(username, 5)) <  int(cek_file_game(game_id, 4)): #if saldo < harga game
            print("Saldo anda tidak cukup untuk membeli Game tersebut!")
            
        else:
            if int(cek_file_game(game_id, 5)) > 0: #if stok > 0
                print("Game "+ '"' + cek_file_game(game_id, 1) + '"' + " berhasil dibeli!")

                file_user = convertToMatriks("data_login.csv")
                file_game = convertToMatriks("store_game.csv")
                pengurangan_saldo(username, game_id, file_user) #Pengurangan saldo user
                pengurangan_stok(game_id, file_game) #Pengurangan stok game

                '''nunggu fungsi save'''
                '''writeRiwayat(game_id) #Tambah riwayat
                writeKepemilikan(game_id) #Tambah kepemilikan'''
            else: #stok = 0
                print("Stok Game tersebut sedang habis!")
    else:
        print("Anda sudah memiliki Game tersebut!")
