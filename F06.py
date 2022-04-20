from functions import *

def ubahStok () :
    import idGame
    X = input("Masukkan ID game: ")
    idGame.validasiIdGame(X, "store_game.csv")
    jumlah = int(input("Masukkan jumlah: "))
    #1.MENGAMBIL LINE DENGAN STOK TIDAK DIUBAH dari file awal
    f=open("store_game.csv", 'r')
    unChanged_line = ""
    data = f.readlines()
    for line in data:
        if (parse(line)[0] != X) :
            unChanged_line = unChanged_line+line
    #2.MEMBACA LINE DENGAN STOK YANG DIUBAH dari file awal
    for line in data:
        if parse(line)[0]==X:  
            arr = parse(line)
            nama= arr[1]
            kategori= arr[2]
            tahun_rilis= arr[3]
            harga= arr[4]
            stokAwal = int(arr[5])
            break
    #3.BUAT ARRAY BERISI LINE YANG SUDAH DIUBAH
    stokBaru = stokAwal+jumlah 
    if stokBaru >= 0 :
        if stokBaru>stokAwal:
            print("Stok game",nama,"berhasil ditambahkan. Stok sekarang:", stokBaru) 
        else:
            print("Stok game",nama,"berhasil dikurangi. Stok sekarang:", stokBaru)     
    else:
        print("Stok game",nama,"gagal dikurangi karena stok kurang. Stok sekarang:",stokAwal)
    Changed_line = ["\n",X,";",nama, ";",kategori,";",tahun_rilis,";",harga,";",str(stokBaru)]
    f.close()
    return [unChanged_line,Changed_line]