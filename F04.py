from functions import *

def tambahGame () :
    import idGame
    f=open("store_game.csv", 'a')
    #Input data game yang ingin ditambahkan
    nama=input("Masukkan nama game: ")
    kategori=input("Masukkan kategori: ")
    tahun_rilis=input("Masukkan tahun rilis: ")
    harga=input("Masukkan harga: ")
    stok=input("Masukkan stok awal: ")
    while ((nama=="") or (kategori=="") or (tahun_rilis=="") or (harga=="") or (stok=="")) :
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        nama=input("Masukkan nama game: ")
        kategori=input("Masukkan kategori: ")
        tahun_rilis=input("Masukkan tahun rilis: ")
        harga=input("Masukkan harga: ")
        stok=input("Masukkan stok awal: ")
    #Generator id game
    gid = "GAME"+(idGame.make_id(tahun_rilis,(float(harga)),stok))
    #Menjadikan semua input dan id game sebagai satu baris dengan array
    lines=["\n", gid, ";", nama,";",kategori,";",tahun_rilis,";",harga,";",stok]
    print("Selamat! Berhasil menambahkan game", nama)
    f.close()
    return lines

#Fungsi untuk update data di file csv 
#[terlanjur dibuat sebelum diinfokan harus menggunakan fungsi save]
def updateLine (lines):
    g=open("store_game.csv", 'a')
    g.writelines(lines)
    g.close()
