def sortingTahun(skema_sorting,dataSources):
    import parse
    import sum_line
    #1. MEMBUAT VARIABEL
    f=open( dataSources, 'r')
    data = f.readlines()
    IndEfektif=((sum_line.banyakBaris( dataSources))-1)
    #2. MENGUMPULKAN TAHUN SEBAGAI MATRIKS
    Msort = ["" for i in range (IndEfektif)]
    i = 0
    for line in data:
        if parse.parse(line,6)[3] != "tahun_rilis" :
            Msort[i] = int(parse.parse(line,6)[3])
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
            if Msort[k]==parse.parse(line,6)[3]:
                arr = parse.parse(line, 6)
                print(arr[0],"|",arr[1],"|",arr[2],"|",arr[3],"|",arr[4],"|",arr[5],"|")    
    f.close()

def sortingHarga(skema_sorting,dataSources):
    import parse
    import sum_line
    #1. READING DATA, BUAT VARIABEL
    f=open(dataSources, 'r')
    data = f.readlines()
    IndEfektif=((sum_line.banyakBaris(dataSources))-1)
    #2. MENGUMPULKAN HARGA SEBAGAI MATRIKS
    Msort = ["" for i in range (IndEfektif)]
    i = 0
    for line in data:
        if parse.parse(line,6)[4] != "harga" :
            Msort[i] = int(parse.parse(line,6)[4])
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
            if Msort[k]==(parse.parse(line,6)[4]):
                arr = parse.parse(line, 6)
                print(arr[0],"|",arr[1],"|",arr[2],"|",arr[3],"|",arr[4],"|",arr[5],"|")    
    f.close()

def sortingID (skema_sorting,dataSources):
    if skema_sorting=="" :
        import parse
        import sum_line
        #1. READING DATA, BUAT VARIABEL
        f=open(dataSources, 'r')
        data = f.readlines()
        #2. MENYIMPAN SEMUA ANGKA ID DALAM STRING
        numId = ""
        for line in data:
            k=parse.parse(line,6)[0]
            for line in k:
                if line!="i" and line!="d" and line!="G":
                    numId = str(numId)+str(line)
        #3. MEMBUAT ARRAY ID
        length = (sum_line.panjangTeks(numId))
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
                if "G"+str(Mid[k])==parse.parse(line,6)[0]:
                    arr = parse.parse(line, 6)
                    print(arr[0],"|",arr[1],"|",arr[2],"|",arr[3],"|",arr[4],"|",arr[5],"|")    
        f.close()


dataSources = "C:\Coding\TubesDaspro\gim.csv"

def listGameToko (dataSources) :
    skema_sorting=input("")
    if skema_sorting=="tahun-" or skema_sorting=="tahun+":
        sortingTahun(skema_sorting,dataSources)
    elif skema_sorting=="harga-" or skema_sorting=="harga+":
        sortingHarga(skema_sorting,dataSources)
    elif skema_sorting=="":
       sortingID (skema_sorting,dataSources) 
    else:
        print("Skema sorting tidak valid!")

listGameToko(dataSources)


