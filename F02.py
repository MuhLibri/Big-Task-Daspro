# F02 - Register
from functions import *
from B01 import *

def register():
    print("Registrasi")
    register_name = input("Masukkan Nama: ")
    register_username = input("Masukkan Username: ")
    register_password = input("Masukkan Password: ")
    while (not cekKarakterUsername(register_username)) or (not cekUsernameLama(register_username)) or (not cekRegKosong(register_name,register_username,register_password)):
        if not cekKarakterUsername(register_username):
            print("Username hanya dapat berisikan alfabet A-Za-z, underscore “_”, strip “-”, dan angka 0-9. Silahkan ulangi registrasi!")
        elif not cekUsernameLama(register_username):
            print("Username telah diambil. Silahkan ulangi registrasi!")
        else: # not cekKosong(register_name,register_username,register_password)
            print("Data registrasi tidak boleh kosong. Silahkan ulangi registrasi!")
        print()
        print("register")
        register_name = input("Masukkan Nama: ")
        register_username = input("Masukkan Username: ")
        register_password = input("Masukkan Password: ")
    regData(register_name,register_username,register_password)
    #makeOwnedList(register_username)
    print("Username %s telah berhasil didaftarkan ke dalam “Binomo”."%register_username)
    return
