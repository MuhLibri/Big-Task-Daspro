from functions import *

def tambahGame () :
    import idGame
    f=open("store_game.csv", 'a')
    #Input data game yang ingin ditambahkan
    nama=input("Masukkan nama game: ")
    kategori=input("Masukkan kategori: ")
    tahun_rilis=int(input("Masukkan tahun rilis: "))
    harga=input("Masukkan harga: ")
    stok=int(input("Masukkan stok awal: "))
    while ((nama=="") or (kategori=="") or (tahun_rilis=="") or (harga=="") or (stok=="")) :
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        nama=input("Masukkan nama game: ")
        kategori=input("Masukkan kategori: ")
        tahun_rilis=int(input("Masukkan tahun rilis: "))
        harga=input("Masukkan harga: ")
        stok=int(input("Masukkan stok awal: "))
    #Generator id game
    gid = "G"+(idGame.make_id(tahun_rilis,(float(harga)),stok))
    #Menjadikan semua input dan id game sebagai satu baris dengan array
    lines=["\n", gid, ";", nama,";",kategori,";",str(tahun_rilis),";",str(harga),";",str(stok)]
    print("Selamat! Berhasil menambahkan game", nama)
    f.close()
    return lines

def updateLine (lines):
    g=open("store_game.csv", 'a')
    g.writelines(lines)
    g.close()