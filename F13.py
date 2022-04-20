from functions import *

def panjang(array): #Fungsi untuk menghitung panjang list/array (menghitung elemen seperti fungsi len())
    k = 0
    for i in array:
        k += 1
    return k

def konsDot(array, element): #Prosedur menambahkan sebuah elemen ke belakang array
    array += [element]

def cek_file_user(username, indeks_kolom): #Fungsi untuk mencari data di user.csv berdasarkan username dan mereturn data berdasarkan indeks_kolom
        file_user = open('data_login.csv', 'r')  #indeks_kolom; saldo = 5, user_id = 0
        read_file = file_user.readline()
        while (read_file != ""):
            if (username == parse(read_file, 6)[2]):
                file_user.close()
                return parse(read_file, 6)[indeks_kolom]
            read_file = file_user.readline()
            
def kepemilikan_game(username : str): #Fungsi untuk membuat list berupa game yang dimiliki user
        file_kepemilikan = open('riwayat.csv', 'r')
        read_file = file_kepemilikan.readline()
        G = []
        userid = cek_file_user(username, 0) #Mendeklarasikan user id yang didapat dari fungsi ke variabel userid
        while (read_file != ""):
                if (userid == parse(read_file, 5)[0]):
                    konsDot(G, parse(read_file, 5)[1])
                read_file = file_kepemilikan.readline()
        file_kepemilikan.close()
        return G

def tampilkan_riwayat(username : str): #Prosedur menampilkan riwayat transaksi user
        file_game = open('riwayat.csv', 'r')
        read_file = file_game.readline()
        print("Daftar Game : ")
        k = 0 #untuk nomor yang keprint
        while (read_file != ""):
            M = parse(read_file)
            G = kepemilikan_game(username) #list game yang dimiliki user
            for i in range(panjang(G)):
                if G[i] == M[1] and cek_file_user(username, 0) == M[0]:
                    M = parse(read_file) #menghilangkan kolom pertama yaitu user_id
                    k += 1
                    print(f"{k}.", end = " ")
                    for i in range(panjang(M)):
                        if i != 0: #menghilangkan kolom pertama yaitu user_id
                            print(M[i], end = " | ")
                    print("\n")
            read_file = file_game.readline()
        file_game.close()

def riwayat(username : str): #Prosedur untuk melihat riwayat user serta beberapa info terkait
    G = kepemilikan_game(username) #Mendeklarasikan list berupa game yang pernah dibeli user yang terdapat di riwayat
    if panjang(G) > 0:
        tampilkan_riwayat(username)
    else: #panjang(G) tidak mungkin negatif sehingga panjang(G) == 0
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
