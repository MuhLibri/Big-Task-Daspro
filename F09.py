from functions import *

def cekOwnedGame(GameID,username):#Fungsi yang melihat apakah user sudah memiliki game tersebut
    M = kepemilikan_game(username)
    for i in range (countLen(M)):
        if (GameID == M[i]):
            return True
    return False

def user_id(username): #Fungsi untuk mencari user id dari username
        file_user = open('data_login.csv', 'r')
        read_file = file_user.readline()
        while (read_file != ""):
            if (username == parse(read_file)[2]):
                file_user.close()
                return parse(read_file)[0]
            read_file = file_user.readline()


def kepemilikan_game(username): #Fungsi untuk membuat list berupa game yang dimiliki user
        file_kepemilikan = open('kepemilikan.csv', 'r')
        read_file = file_kepemilikan.readline()
        G = []
        userid = user_id(username) #Mendeklarasikan user id yang didapat dari fungsi user_id() ke variabel userid
        while (read_file != ""):
                if (userid == parse(read_file)[1]):
                    konsDot(G, parse(read_file)[0])
                read_file = file_kepemilikan.readline()
        file_kepemilikan.close()
        return G

def list_game(): #Prosedur untuk melihat game yang dimiliki user serta beberapa info terkait
    username = "haqufa" #hanya sebagai contoh jika tidak di main program
    longest_name = lenMax(1)
    longest_genre = lenMax(2)
    game_info = open("store_game.csv",'r')
    search_game = game_info.readline()
    num = 1
    print("Daftar game: ")
    while (search_game != ""):
        if cekOwnedGame(parse(search_game)[0],username):
            tampilkan_game_dimiliki(num,parse(search_game)[0],parse(search_game)[1],parse(search_game)[2],parse(search_game)[3],parse(search_game)[4],longest_name,longest_genre)
            num = num + 1
        search_game = game_info.readline()
    if (num == 1):
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
    game_info.close()
    return
