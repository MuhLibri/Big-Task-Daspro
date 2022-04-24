import os
import csv
from functions import *
def save(user, game, riwayat, kepemilikan):
    jumlah_user = jumlah(user)
    jumlah_game = jumlah(game)
    jumlah_riwayat = jumlah(riwayat)
    jumlah_kepemilikan = jumlah(kepemilikan)
    savename = input('Masukkan Nama folder: ')
    try:
        os.mkdir("./"+savename)
    except OSError as e:
        print("Nama Folder sudah ada")

    with open('./'+savename+'user.csv','w', newline='') as userfile:
        head = ['userid','username','nama','password','role','saldo']
        isiuser = csv.DictWriter(userfile,fieldnames=head,delimiter=',')
        for i in range (jumlah_user):
            if i==0 :
                isiuser.writeheader()
            else:
                isiuser.writerow({'userid':user[i][0], 'username':user[i][1], 'nama':user[i][2], 'password':user[i][3], 'role':user[i][4], 'saldo':user[i][5]})

    with open('./'+savename+'game.csv','w', newline='') as gamefile:
        head = ['id','nama','kategori','tahun rilis','harga','stok']
        isigame = csv.DictWriter(gamefile,fieldnames=head,delimiter=',')
        for i in range (jumlah_game):
            if i==0 :
                isigame.writeheader()
            else:
                isigame.writerow({'id':game[i][0], 'nama':game[i][1], 'kategori':game[i][2], 'tahun rilis':game[i][3], 'harga':game[i][4], 'stok':game[i][5]})

    with open('./'+savename+'/riwayat.csv','w', newline='') as riwayatfile:
        head = ['gameid','nama','harga','userid','tahun beli']
        isiriwayat = csv.DictWriter(riwayatfile,fieldnames=head,delimiter=',')
        for i in range (jumlah_riwayat):
            if i==0 :
                isiriwayat.writeheader()
            else:
                isiriwayat.writerow({'gameid':riwayat[i][0], 'nama':riwayat[i][1], 'harga':riwayat[i][2], 'user_id':riwayat[i][3], 'tahun_beli':riwayat[i][4]})

    with open('./'+savename+'kepemilikan.csv','w', newline='') as kepemilikan_file:
        head = ['gameid','userid']
        isikepemilikan = csv.DictWriter(kepemilikan_file,fieldnames=head,delimiter=',')
        for i in range (jumlah_kepemilikan):
            if i==0 :
                isikepemilikan.writeheader()
            else:
                isikepemilikan.writerow({'gameid':kepemilikan[i][0], 'userid':kepemilikan[i][1]})
