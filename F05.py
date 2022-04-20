# F05
from functions import *

def ubahGame ():
    X = input("Masukkan ID game: ")
    nama=input("Masukkan nama game: ")
    kategori=input("Masukkan kategori: ")
    tahun_rilis=input("Masukkan tahun rilis: ")
    harga=input("Masukkan harga: ")
    #1.MENGAMBIL LINE YANG TIDAK DIUBAH dari file awal
    f=open("store_game.csv", 'r')
    unChanged_line = ""
    data = f.readlines()
    for line in data:
        if (parse(line)[0] != X) :
            unChanged_line = unChanged_line+line
    #2.BACA LINE YANG DIUBAH dari file awal
    for line in data:
        if parse(line)[0]==X: 
            arr = parse(line)
            namaAwal = arr[1]
            kategoriAwal = arr[2]
            tahun_rilisAwal= arr[3]
            hargaAwal = arr[4]
            stokAwal = arr[5]
            break
    #3. BUAT ARRAY BERISI LINE YANG SUDAH DIUBAH
    if nama!="" :
        namaAwal = nama
    if kategori!="" :
        kategoriAwal = kategori
    if tahun_rilis!="" :
        tahun_rilisAwal = tahun_rilis
    if harga!="" :
        hargaAwal = harga
    Changed_line = ["\n",X,";",namaAwal, ";",kategoriAwal,";",tahun_rilisAwal,";",hargaAwal,";",stokAwal]
    f.close()
    return [unChanged_line,Changed_line]

def updateFile (unChanged_line,Changed_line,newFile) :
    g=open(newFile, 'w')
    g.writelines(unChanged_line)
    g.close()
    g=open(newFile, 'a')
    g.writelines(Changed_line)
    g.close()

