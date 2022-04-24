from functions import *

def cek_file_user(username, indeks_kolom): #Fungsi untuk mencari data di data_login.csv berdasarkan username dan mereturn data berdasarkan indeks_kolom
        file_user = open('data_login.csv', 'r')  #indeks_kolom; saldo = 5, user_id = 0
        read_file = file_user.readline()
        while (read_file != ""):
            if (username == parse(read_file)[2]):
                file_user.close()
                return parse(read_file)[indeks_kolom]
            read_file = file_user.readline()
            
def kepemilikan_game(username): #Fungsi untuk membuat list berupa game yang dimiliki user
        file_kepemilikan = open('riwayat.csv', 'r')
        read_file = file_kepemilikan.readline()
        G = []
        userid = cek_file_user(username, 0) #Mendeklarasikan user id yang didapat dari fungsi ke variabel userid
        while (read_file != ""):
                if (userid == parse(read_file)[0]):
                    konsDot(G, parse(read_file)[1])
                read_file = file_kepemilikan.readline()
        file_kepemilikan.close()
        return G

def tampilkan_riwayat(username): #Prosedur menampilkan riwayat transaksi user
        file_game = open('riwayat.csv', 'r')
        read_file = file_game.readline()
        print("Daftar Game : ")
        k = 0 #untuk nomor yang keprint
        while (read_file != ""):
            M = parse(read_file)
            G = kepemilikan_game(username) #list id game dari game yang dimiliki user
            for i in range(countLen(G)):
                if G[i] == M[1] and cek_file_user(username, 0) == M[0]:
                    M = parse(read_file)
                    k += 1
                    print(f"{k}.", end = " ")
                    for i in range(countLen(M)):
                        if i != 0: #menghilangkan kolom pertama yaitu user_id
                            print(M[i], end = " | ")
                    print("\n")
            read_file = file_game.readline()
        file_game.close()

def riwayat(username): #Prosedur untuk melihat riwayat user serta beberapa info terkait
    G = kepemilikan_game(username) #Mendeklarasikan list berupa game yang pernah dibeli user yang terdapat di riwayat
    if countLen(G) > 0:
        tampilkan_riwayat(username)
    else: #countLen(G) tidak mungkin negatif sehingga counLen(G) == 0
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
