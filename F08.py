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

def cek_kepemilikan(game_id, username):
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

def newStringRiwayat(username,game_id):
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

def writeRiwayat(game_id):
    new_data = newStringRiwayat(game_id)
    file_riwayat = open("riwayat.csv",'w')
    write_riwayat = file_riwayat.write(new_data)
    file_riwayat.close()
    return write_riwayat

def newStringKepemilikan(username,game_id):
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

def writeKepemilikan(game_id):
    new_data = newStringKepemilikan(game_id)
    file_kepemilikan = open("kepemilikan.csv",'w')
    write_kepemilikan = file_kepemilikan.write(new_data)
    file_kepemilikan.close()
    return write_kepemilikan

def gantiChar(word , a, b): #Fungsi yang mengganti suatu character a menjadi character baru b pada suatu string/word #COMPLETE
    new_string = "" #prekondisi awal string kosong
    for char in word:
        if char != a:
            new_string += char
        else:
            new_string += b
    return new_string

def homemade_split(word, delimiter): #Fungsi yang mengubah string menjadi elemen pada array yang dipisahkan oleh delimiter
    jmlh_elmt = 1                     
    for i in word:
        if i == delimiter:
            jmlh_elmt += 1
    li = [" " for i in range(jmlh_elmt)]
    new_string = ""
    indeks = 0
    j = 0
    for character in word:
        if character != delimiter:
            new_string += character
            if (j == countLen(word)-1):
                li[indeks] = new_string
        else:
            li[indeks] = new_string
            new_string = ""
            indeks += 1
        j += 1
    return li

def convertToMatriks(nama_file):#Fungsi yang mengubah data file csv menjadi matriks
    file_open = open(nama_file, "r")
    reads_file = file_open.readlines()
    file_open.close()

    G = [gantiChar(line, "\n", "") for line in reads_file]
    matriks_csv = [[] for i in range(countLen(G))] #Deklarasi matriks berupa list untuk list kosong yang akan diisi elemen
    i = 0
    for line in G:
        matriks_csv[i] = homemade_split(line, ";")
        i += 1
    return matriks_csv

def cek_data(matriks_csv, elmt, kolom): #Fungsi yang mengecek apakah suatu elemen terdapat pada kolom matriks tertentu
    existence = False
    for line in matriks_csv:
        if line[kolom] == elmt:
            existence = True
            break
    return existence

def find_indeks(matriks_csv, elmt, kolom): #Fungsi yang menghasilkan indeks di mana pertama kali suatu elemen pada kolom ditemukan
    i = 0
    while elmt != matriks_csv[i][kolom] and i < (countLen(matriks_csv)-1):
        i += 1
    return i #indeks

def pengurangan_saldo_procedure(username, game_id, matriks_csv): #Prosedur topup saldo user
    indeks = find_indeks(matriks_csv, username, 2)
    matriks_csv[indeks][5] = str(int(matriks_csv[indeks][5]) - int(cek_file_game(game_id, 4))) #Assign saldo baru ke saldo lama (hanya dalam memori) sebelum disave
    print(f"Saldo menjadi {(matriks_csv[indeks][5])}.")
    return matriks_csv

def pengurangan_stok_procedure(game_id, matriks_csv): #Prosedur pengurangan stok game
    indeks = find_indeks(matriks_csv, game_id, 0)#
    matriks_csv[indeks][5] = str(int(matriks_csv[indeks][5]) - 1) #Assign stok baru ke stok lama (hanya dalam memori) sebelum disave
    print(f"Stok menjadi {(matriks_csv[indeks][5])}.")
    return matriks_csv


def buy_game(username):
    game_id = input("Masukan game id : ")
    if not (cek_kepemilikan(game_id, username)):
        userid = cek_file_user(username, 0)
        if int(cek_file_user(username, 5)) <  int(cek_file_game(game_id, 4)): #if saldo < harga game
            print("Saldo anda tidak cukup untuk membeli Game tersebut!")
            
        else:
            if int(cek_file_game(game_id, 5)) > 0: #if stok > 0
                print("Game "+ '"' + cek_file_game(game_id, 2) + '"' + " berhasil dibeli!")

                file_user = convertToMatriks("data_login.csv")
                file_game = convertToMatriks("store_game.csv")
                pengurangan_saldo_procedure(username, game_id, file_user) #Pengurangan saldo user
                pengurangan_stok_procedure(game_id, file_game) #Pengurangan stok game

                '''writeRiwayat(game_id) #Tambah riwayat
                writeKepemilikan(game_id) #Tambah kepemilikan'''
            else: #stok = 0
                print("Stok Game tersebut sedang habis!")
    else:
        print("Anda sudah memiliki Game tersebut!")