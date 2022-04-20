# F03 - Login
from functions import *

def login():
    print("Login")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    password = encript(password,keyGenerator(password))

    while not (CekLogin(username, password)):
        print("Password atau username salah atau tidak ditemukan.")
        print()
        print("Login")
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        password = encript(password,keyGenerator(password))

    print("Halo %s! Selamat datang di “Binomo”."%cariNama(username))
    role = cariRole(username)
    return username,password,role