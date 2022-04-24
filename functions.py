# Branch Functions
from B01 import *

def parse(line):            # Pengganti split(). Untuk parsing
    data_num = 1
    for word in line:
        if (word == ";"):
            data_num = data_num + 1
    Array = ["" for i in range(data_num)]
    i = 0
    for word in line:
            if (word != ";") and (word != "\n"):
                Array[i] = Array[i] + word
            else:
                i = i + 1
    return Array

def countLen(line):         # Pengganti fungsi len()
    count = 0
    for word in line:
        count = count + 1
    return count

def CekLogin(username, password):       # Mengecek apakah username dan password yang dimasukin benar atau salah
    login_info = open("data_login.csv",'r')
    read_login = login_info.readline()
    read_login = login_info.readline()
    while (read_login != ""):
        if (username == parse(read_login)[2]) and (password == parse(read_login)[3]):
            login_info.close()
            return True
        read_login = login_info.readline()
    login_info.close()
    return False

def cariNama(username):             # Mencari nama pengguna berdasarkan username
    login_info = open("data_login.csv",'r')
    read_login = login_info.readline()
    read_login = login_info.readline()
    while (read_login != ""):
        if (username == parse(read_login)[2]):
            login_info.close()
            return parse(read_login)[1]
        read_login = login_info.readline()

def cariRole(username):         # Mencari role pengguna berdasarkan username
    login_info = open("data_login.csv",'r')
    read_login = login_info.readline()
    read_login = login_info.readline()  
    while (read_login != ""):
        if (username == parse(read_login)[2]):
            login_info.close()
            return parse(read_login)[4]
        read_login = login_info.readline()

def validUsername(word):        # Mengecek per huruf apakah valid atau tidak
    return (65 <= ord(word) <= 90) or (97 <= ord(word) <= 122) or (word == "_") or (word == "-") or (48 <= ord(word) <= 57)

def cekKarakterUsername(register_username):     # Mengecek seluruh karakter pada username yang akan diregistrasikan
    for word in register_username:
        if not validUsername(word):
            return False
    return True

def cekUsernameLama(register_username):         # Mengecek apakah username sudah ada atau belum
    register_info = open("data_login.csv",'r')
    read_register = register_info.readline()
    read_register = register_info.readline()
    while (read_register != ""):
        if (register_username == parse(read_register)[2]):
            register_info.close()
            return False
        read_register = register_info.readline()
    register_info.close()
    return True

def cekRegKosong(a,b,c):
    return (a != "") and (b != "") and (c != "")

def addLastID():        # Menambah 1 angka ID terakhir untuk setiap ID baru yang diregistrasikan
    register_info = open("data_login.csv",'r')
    read_register = register_info.readline()
    read_register = register_info.readline()
    while (read_register != ""):
        last_id = parse(read_register)[0]
        read_register = register_info.readline()
    register_info.close()
    last_id = int(last_id) + 1
    return str(last_id)       

def newStringData(register_name,register_username,register_password):       # String data baru
    new_reg = addLastID() + ";" + register_name + ";" + register_username + ";" + encript(register_password,keyGenerator(register_password)) + ";" + "user" + ";" + "0"
    new_string = ""
    register_info = open("data_login.csv",'r')
    read_register = register_info.readline()
    while (read_register != ""):
        new_string = new_string + read_register
        read_register = register_info.readline()
    new_string = new_string + "\n" + new_reg
    register_info.close()
    return new_string

def regData(register_name,register_username,register_password):         # Meregistrasikan semua data baru ke data_login.csv
    new_data = newStringData(register_name,register_username,register_password)
    register_info = open("data_login.csv",'w')
    write_register = register_info.write(new_data)
    register_info.close()
    return

def cariID(username):           # Mencari ID pengguna berdasarkan username
    login_info = open("data_login.csv",'r')
    read_login = login_info.readline()
    while (read_login != ""):
        if (username == parse(read_login)[2]):
            login_info.close()
            return parse(read_login)[0]
        read_login = login_info.readline()

def tampilkan_game_dimiliki(num,a,b,c,d,e,ln,lg):       # Menampilkan game yang dimiliki
    if countLen(str(num)) == 1:
        print("%i."%num, "  ", a, "|", b, "%s|"%(" " *(ln-countLen(b))), c, "%s|"%(" " *(lg-countLen(c))), d, "|", e)
    elif countLen(str(num)) == 2:
        print("%i."%num, " ", a, "|", b, "%s|"%(" " *(ln-countLen(b))), c, "%s|"%(" " *(lg-countLen(c))), d, "|", e)
    else:
        print("%i."%num, "", a, "|", b, "%s|"%(" " *(ln-countLen(b))), c, "%s|"%(" " *(lg-countLen(c))), d, "|", e)
    return

def cleanPrintStore(num,a,b,c,d,e,f,ln,lg,lp):      # Menampilkan Game di toko
    if countLen(str(num)) == 1:
        print("%i."%num, "  ", a, "|", b, "%s|"%(" " *(ln-countLen(b))), c, "%s|"%(" " *(lg-countLen(c))), d, "|", e, "%s|"%(" " *(lp-countLen(e))), f)
    elif countLen(str(num)) == 2:
        print("%i."%num, " ", a, "|", b, "%s|"%(" " *(ln-countLen(b))), c, "%s|"%(" " *(lg-countLen(c))), d, "|", e, "%s|"%(" " *(lp-countLen(e))), f)
    else:
        print("%i."%num, "", a, "|", b, "%s|"%(" " *(ln-countLen(b))), c, "%s|"%(" " *(lg-countLen(c))), d, "|", e, "%s|"%(" " *(lp-countLen(e))), f)
    return

def lenMax(index):        # Mencari kata-kata terpanjang
    game_info = open("store_game.csv",'r')
    search_game = game_info.readline()
    search_game = game_info.readline()
    max = 0
    while (search_game != ""):
        if max < countLen(parse(search_game)[index]):
            max = countLen(parse(search_game)[index])
        search_game = game_info.readline()
    game_info.close()
    return max

def cekExit(s):         # Mengecek masukan untuk exit
    return ((s == "Y") or (s == "y") or (s == "N") or (s == "n"))

# Bonus Branch
def hurufKecil(word):
    return (97 <= ord(word) <= 122)

def hurufBesar(word):
    return (65 <= ord(word) <= 90)

def angka(word):
    return (48 <= ord(word) <= 57)

def keyGenerator(line):
    key = countLen(line)
    if key > 8:
       while key > 8: 
           key = (key % 10) + 1
    return key

def random(pertanyaan,faktor_random):       # randomizer untuk magic conch
    j = countLen(pertanyaan) + faktor_random
    while j > 12:
        j = (j % 10) + 1
    return j

def printBoard(P):      # Menampilkan papan permainan
    print("\nStatus Papan")
    for i in range (3):
        for j in range (3):
            print(P[i][j], end = "")
        print()
    print()
    return

def cekInput(x,y):      # Memeriksa input dari pemain
    return (1 <= x <= 3) and (1 <= y <= 3)

def cekFilled(P,x,y):       # Memeriksa apakah kotak yang diisi pemain sudah terisi atau belum
    for i in range (3):
        for j in range (3):
            if (i == (y-1)) and (j == (x-1)):
                if (P[i][j] == "X") or (P[i][j] == "O"):
                    return False
    return True

def play(P,player):         # Mengolah permainan
    x = int(input("X: "))
    y = int(input("Y: "))
    while not (cekInput(x,y) and cekFilled(P,x,y)):
        if not cekFilled(P,x,y):
            print("Kotak ini sudah terisi. Silahkan isi kotak lain! ")
        elif not cekInput(x,y):
            print("Masukan tidak valid. Silahkan masukkan kembali!")
        x = int(input("X: "))
        y = int(input("Y: "))
    for i in range (3):
        for j in range (3):
            if (i == (y-1)) and (j == (x-1)):
                P[i][j] = player
    return P

def cekFull(P):     # Memeriksa apakah papan sudah penuh atau belum
    for i in range (3):
        for j in range (3):
            if (P[i][j] == "#"):
                return False
    return True

def cekWin(P,pl):       # Memeriksa kemenangan
    # Menang Horizontal
    if (pl == P[0][0] == P[0][1] == P[0][2]):
        return True
    elif (pl == P[1][0] == P[1][1] == P[1][2]):
        return True
    elif (pl == P[2][0] == P[2][1] == P[2][2]):
        return True
    # Menang Vertikal
    elif (pl == P[0][0] == P[1][0] == P[2][0]):
        return True
    elif (pl == P[0][1] == P[1][1] == P[2][1]):
        return True
    elif (pl == P[0][2] == P[1][2] == P[2][2]):
        return True
    # Menang diagonal
    elif (pl == P[0][0] == P[1][1] == P[2][2]):
        return True
    elif (pl == P[0][2] == P[1][1] == P[2][0]):
        return True 
    return False

def Array(arr1, item):
    
    return arr1 + item

def panjang(item):

    counter = 0
    for _ in item:
        counter += 1
    return counter

def overwrite(nama_file, matriks):
    with open(nama_file, 'w+') as data:
        for i in range(panjang(matriks)):
            line = ""
            for j in range(panjang(matriks[i])):
                line += str(matriks[i][j])
                if j != panjang(matriks[i]) - 1:
                    line += ';'
            if (i != (panjang(matriks) - 1)):
                line += '\n'
            data.write(line)

def konsDot(array, element): #Prosedur menambahkan sebuah elemen ke belakang array
    array += [element]

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

def cek_data(matriks_csv, elmt, kolom): #Fungsi yang mengecek apakah suatu elemen terdapat pada kolom matriks tertentu
    existence = False
    for line in matriks_csv:
        if line[kolom] == elmt:
            existence = True
            break
    return existence

def gantiChar(word , a, b): #Fungsi yang mengganti suatu character a menjadi character baru b pada suatu string/word #COMPLETE
    new_string = "" #prekondisi awal string kosong
    for char in word:
        if char != a:
            new_string += char
        else:
            new_string += b
    return new_string

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

def find_indeks(matriks_csv, elmt, kolom): #Fungsi yang menghasilkan indeks di mana pertama kali suatu elemen pada kolom ditemukan
    i = 0
    while elmt != matriks_csv[i][kolom] and i < (countLen(matriks_csv)-1):
        i += 1
    return i #indeks
