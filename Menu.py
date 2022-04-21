from B01 import *
from B02 import *
from B03 import *
from F02 import *
from F03 import *
from F04 import *
from F05 import *
from F06 import *
from F07 import *
from F08 import *
from F09 import *
from F10 import *
from F11 import *
from F12 import *
from F13 import *
from F14 import *
from F15 import *
from F16 import *
from F17 import *

# Menu
def mainMenu(role,username):
    print("\n                                                       Menu Utama\n")
    print("01 Registrasi                                                            09 Cari Game di Toko dari ID, Nama Game, Harga, Kategori dan Tahun Rilis")
    print("02 Tambah Game ke Toko                                                   10 Top Up")
    print("03 Ubah Game pada Toko                                                   11 Riwayat Pembelian")
    print("04 Ubah Stok Game pada Toko                                              12 Ekstra")
    print("05 List Game di Toko berdasarkan ID, Tahun Rilis, dan Harga              13 Help")
    print("06 Beli Game                                                             14 Load")
    print("07 Lihat Game yang Dimiliki                                              15 Save")
    print("08 Cari Game yang dimiliki dari ID dan Tahun Rilis                       16 Exit\n")
    c = input()
    print()
    if (c == "01"):
        if (role == "admin"):
            register()
        else: # role == "user"
            print("Maaf, fungsi ini hanya dapat diakses oleh admin")
    elif (c == "02"):
        if (role == "admin"):
            tambahGame()
        else: # role == "user"
            print("Maaf, fungsi ini hanya dapat diakses oleh admin")
    elif (c == "03"):
        if (role == "admin"):
            ubahGame ()
        else: # role == "user"
            print("Maaf, fungsi ini hanya dapat diakses oleh admin")
    elif (c == "04"):
        if (role == "admin"):
            ubahStok ()
        else: # role == "user"
            print("Maaf, fungsi ini hanya dapat diakses oleh admin")
    elif (c == "05"):
        listGameToko ()         
    elif (c == "06"):
        if (role == "user"):
            buy_game(username)
        else: # role == "admin"
            print("Maaf, fungsi ini hanya dapat diakses oleh user")
    elif (c == "07"):
        if (role == "user"):
            list_game(username)
        else: # role == "admin"
            print("Maaf, fungsi ini hanya dapat diakses oleh user")
    elif (c == "08"):
        if (role == "user"):
            ownedIDYR(username)
        else: # role == "admin"
            print("Maaf, fungsi ini hanya dapat diakses oleh user")
    elif (c == "09"):
        storeGameSearch()
    elif (c == "10"):
        if (role == "admin"):
            topup(convertToMatriks("data_login.csv"))
        else: # role == "user"
            print("Maaf, fungsi ini hanya dapat diakses oleh admin")
    elif (c == "11"):
        if (role == "user"):
            riwayat(username)
        else: # role == "admin"
            print("Maaf, fungsi ini hanya dapat diakses oleh user")
    elif (c == "11"):
        if (role == "user"):
            riwayat(username)
        else: # role == "admin"
            print("Maaf, fungsi ini hanya dapat diakses oleh user")
    elif (c == "12"):
        menuEkstra()
    elif (c == "13"):
        help()
    elif (c == "14"):
        load(name_folder)
    elif (c == "15"):
        save(user, game, riwayat, kepemilikan)  
    elif (c == "16"):
        exit()
        return
    else:
        print("Masukan tidak valid")
    mainMenu(role,username)

def menuEkstra():
    print("                                                       Menu Ekstra\n")
    print("01 Kerang Ajaib")
    print("02 Tic-Tac-Toe")
    print("03 Menu Utama\n")
    c = input()
    print()
    if (c == "01"):
        B02()
    elif (c == "02"):
        B03()
    elif (c == "03"):
        return
    else:
        print("Masukan tidak valid")
    print()
    menuEkstra()
