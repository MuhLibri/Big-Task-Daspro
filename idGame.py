from functions import *

def make_id (a, b, c) :
    num_id = ""
    for i in range (1, 4):
        z = (a**(i+2)/((b**i)*c**(i+1))) * (a**(i+1)/(b+c))
        while z > 10 :
            z = z%10
        num_id = num_id+str(int(z))
    return num_id

def validasiIdGame(x, dataSource) :
    count=0
    f=open(dataSource, 'r')
    d = f.readlines()
    for line in d:
        d1 = parse(line)[0]
        if d1 == x :
            count=count+1
    f.close()
    if count==0 :
        print("Tidak ada game dengan ID tersebut!")

