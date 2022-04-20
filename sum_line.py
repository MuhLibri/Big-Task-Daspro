def banyakBaris (dataSource):
    f=open(dataSource, 'r')
    data = f.readlines()
    sumOfLine = 0
    for line in data:
        sumOfLine = sumOfLine + 1
    return(sumOfLine)

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

        
