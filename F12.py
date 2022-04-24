from functions import *

def topup_procedure(username, saldo_topup, matriks_csv): #Prosedur topup saldo user
    while not cek_data(matriks_csv, username, 2):
        print(f"Username “{username}” tidak ditemukan.")
        username = input("Masukan username : ")

    indeks = find_indeks(matriks_csv, username, 2)
    while (int(matriks_csv[indeks][5]) + saldo_topup) < 0:
        print("Masukan tidak valid.")
        saldo_topup = int(input("Masukan saldo : "))

    matriks_csv[indeks][5] = str(int(matriks_csv[indeks][5]) + saldo_topup) #Assign saldo baru ke saldo lama (hanya dalam memori) sebelum disave
    nama = matriks_csv[indeks][2]
    if saldo_topup > 0:
        print(f"Top up berhasil. Saldo {nama} bertambah menjadi {(matriks_csv[indeks][5])}.")
    elif saldo_topup == 0:
        print(f"Saldo {nama} tidak ditambah sehingga saldo tetap {(matriks_csv[indeks][5])}.")
    else: #saldo_topup < 0 (saldo total sudah divalidasi sebelumnya)
        print(f"Saldo {nama} telah dikurangi sebesar {abs(saldo_topup)} sehingga tersisa {(matriks_csv[indeks][5])}.")
    return

def topup(): #Prosedur input username dan saldo top up
    matriks_csv = convertToMatriks("data_login.csv")
    username = input("Masukan username : ")
    saldo_topup = int(input("Masukan saldo : "))
    topup_procedure(username, saldo_topup, matriks_csv)
