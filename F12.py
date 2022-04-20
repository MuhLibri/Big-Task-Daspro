from functions import *

def gantiChar(word , a, b): #Fungsi yang mengganti suatu character a menjadi character baru b pada suatu string/word #COMPLETE
    new_string = "" #prekondisi awal string kosong
    for char in word:
        if char != a:
            new_string += char
        else:
            new_string += b
    return new_string

def homemade_split(word, delimiter): #Fungsi yang mengubah string menjadi elemen pada array yang dipisahkan oleh delimiter
    jmlh_elmt = 1                     
    for i in word:
        if i == delimiter:
            jmlh_elmt += 1
    li = [" " for i in range(jmlh_elmt)]
    new_string = ""
    indeks = 0
    j = 0
    for character in word:
        if character != delimiter:
            new_string += character
            if (j == countLen(word)-1):
                li[indeks] = new_string
        else:
            li[indeks] = new_string
            new_string = ""
            indeks += 1
        j += 1
    return li

def convertToMatriks(nama_file):#Fungsi yang mengubah data file csv menjadi matriks
    file_open = open(nama_file, "r")
    reads_file = file_open.readlines()
    file_open.close()

    G = [gantiChar(line, "\n", "") for line in reads_file]
    matriks_csv = [[] for i in range(countLen(G))] #Deklarasi matriks berupa list untuk list kosong yang akan diisi elemen
    i = 0
    for line in G:
        matriks_csv[i] = homemade_split(line, ";")
        i += 1
    return matriks_csv  

def cek_data(matriks_csv, elmt, kolom): #Fungsi yang mengecek apakah suatu elemen terdapat pada kolom matriks tertentu
    existence = False
    for line in matriks_csv:
        if line[kolom] == elmt:
            existence = True
            break
    return existence

def find_indeks(matriks_csv, elmt, kolom): #Fungsi yang menghasilkan indeks di mana pertama kali suatu elemen pada kolom ditemukan
    i = 0
    while elmt != matriks_csv[i][kolom] and i < (countLen(matriks_csv)-1):
        i += 1
    return i #indeks

#########################################################################################################################

def topup_procedure(username, saldo_topup, matriks_csv): #Prosedur topup saldo user
    while not cek_data(matriks_csv, username, 2):
        print(f"Username “{username}” tidak ditemukan.")
        username = input("Masukan username : ")

    indeks = find_indeks(matriks_csv, username, 2)
    while (int(matriks_csv[indeks][5]) + saldo_topup) < 0:
        print("Masukan tidak valid.")
        saldo_topup = int(input("Masukan saldo : "))

    matriks_csv[indeks][5] = str(int(matriks_csv[indeks][5]) + saldo_topup) #Assign saldo baru ke saldo lama (hanya dalam memori) sebelum disave
    matriks_csv[indeks][2]  = nama

    if saldo_topup > 0:
        print(f"Top up berhasil. Saldo {nama} bertambah menjadi {(matriks_csv[indeks][5])}.")
    elif saldo_topup == 0:
        print(f"Saldo {nama} tidak ditambah sehingga saldo tetap {(matriks_csv[indeks][5])}.")
    else: #saldo_topup < 0 (saldo total sudah divalidasi sebelumnya)
        print(f"Saldo {nama} telah dikurangi sebesar {abs(saldo_topup)} sehingga tersisa {(matriks_csv[indeks][5])}.")
    return

def topup(matriks_csv): #Prosedur input username dan saldo top up
    username = input("Masukan username : ")
    saldo_topup = int(input("Masukkan saldo: "))
    topup_procedure(username, saldo_topup, matriks_csv)


# '''Contoh Pemakaian :'''
# topup(convertToMatriks("user.csv"))

