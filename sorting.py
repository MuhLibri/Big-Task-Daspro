from functions import*
from sum_line import*

def sortingTahun(skema_sorting):
    #1. MEMBUAT VARIABEL
    f=open("store_game.csv", 'r')
    data = f.readlines()
    IndEfektif=(banyakBaris("store_game.csv"))-1
    #2. MENGUMPULKAN TAHUN SEBAGAI MATRIKS
    Msort = ["" for i in range (IndEfektif)]
    i = 0
    for line in data:
        if parse(line)[3] != "tahun_rilis" :
            Msort[i] = int(parse(line)[3])
            #print(Msort[i])
            i = i+1
    #3. SORTING TAHUN DALAM MATRIKS
    if IndEfektif>1 :
        for i in range(IndEfektif-1):
            IMax = i
            for j in range(i+1,IndEfektif):
                if skema_sorting == "tahun-" :
                    if (int(Msort[IMax])<int(Msort[j])):
                        IMax = j
                elif skema_sorting== "tahun+" :
                    if (int(Msort[IMax])>int(Msort[j])):
                        IMax = j
            temp = str(Msort[IMax])
            Msort[IMax] = str(Msort[i])
            Msort[i] = str(temp)
    #4. MENULISKAN KE LAYAR
    for k in range (IndEfektif) :
        for line in data: 
            if Msort[k]== parse(line)[3]:
                arr = parse(line)
                print(arr[0],"|",arr[1],"|",arr[2],"|",arr[3],"|",arr[4],"|",arr[5],"|")    
    f.close()

def sortingHarga(skema_sorting):
    #1. READING DATA, BUAT VARIABEL
    f=open("store_game.csv", 'r')
    data = f.readlines()
    IndEfektif=(banyakBaris("store_game.csv"))-1
    #2. MENGUMPULKAN HARGA SEBAGAI MATRIKS
    Msort = ["" for i in range (IndEfektif)]
    i = 0
    for line in data:
        if parse(line)[4] != "harga" :
            Msort[i] = int(parse.parse(line)[4])
            i = i+1
    #3. SORTING HARGA DALAM MATRIKS
    if IndEfektif>1 :
        for i in range(IndEfektif-1):
            IMax = i
            for j in range(i+1,IndEfektif):
                if skema_sorting=="harga-" :
                    if (int(Msort[IMax])<int(Msort[j])):
                        IMax = j
                elif skema_sorting=="harga+" :
                    if (int(Msort[IMax])>int(Msort[j])):
                        IMax = j
            temp = str(Msort[IMax])
            Msort[IMax] = str(Msort[i])
            Msort[i] = str(temp)
    #4. MENULISKAN KE LAYAR
    for k in range (IndEfektif) :
        for line in data: 
            if Msort[k]==(parse(line)[4]):
                arr = parse(line)
                print(arr[0],"|",arr[1],"|",arr[2],"|",arr[3],"|",arr[4],"|",arr[5],"|")    
    f.close()

def sortingID (skema_sorting):
    if skema_sorting=="" :
        #1. READING DATA, BUAT VARIABEL
        f=open("store_game.csv", 'r')
        data = f.readlines()
        #2. MENYIMPAN SEMUA ANGKA ID DALAM STRING
        numId = ""
        for line in data:
            k=parse(line)[0]
            for line in k:
                if line!="i" and line!="d" and line!="G":
                    numId = str(numId)+str(line)
        #3. MEMBUAT ARRAY ID
        length = (panjangTeks(numId))
        IndEfektif=int(length/3)
        Mid = [0 for i in range(IndEfektif)]
        j=0
        for i in range (IndEfektif):
            Mid[i] = int(numId[j]+numId[j+1]+numId[j+2])
            j=j+3
        #4.SORTING ID ASCENDING
        if IndEfektif>1 :
            for i in range(IndEfektif-1):
                IMax = i
                for j in range(i+1,IndEfektif): 
                    if (int(Mid[IMax])>int(Mid[j])):
                        IMax = j
                temp = (Mid[IMax])
                Mid[IMax] = (Mid[i])
                Mid[i] = (temp)
        #5. MENULISKAN KE LAYAR
        for k in range (IndEfektif) :
            for line in data: 
                if "GAME"+str(Mid[k])==parse(line)[0]:
                    arr = parse(line)
                    print(arr[0],"|",arr[1],"|",arr[2],"|",arr[3],"|",arr[4],"|",arr[5],"|")    
        f.close()
