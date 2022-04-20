from sorting import *

def listGameToko () :
    skema_sorting=input("")
    if skema_sorting=="tahun-" or skema_sorting=="tahun+":
        sortingTahun(skema_sorting)
    elif skema_sorting=="harga-" or skema_sorting=="harga+":
        sortingHarga(skema_sorting)
    elif skema_sorting=="":
       sortingID(skema_sorting) 
    else:
        print("Skema sorting tidak valid!")



