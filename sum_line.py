def banyakBaris (dataSource):
    import parse
    f=open(dataSource, 'r')
    data = f.readlines()
    sumOfLine = 0
    for line in data:
        sumOfLine = sumOfLine + 1
    return(sumOfLine)

#print(banyakBaris("C:\Coding\TubesDaspro\gim.csv"))

def panjangTeks(teks):
    length = 0
    i = 0
    try:
        while teks[i]!="":
            length = length+1
            i=i+1
    except:
        length=length
    return(length)

#print(panjangTeks("ABCDEFGHIJK"))

        