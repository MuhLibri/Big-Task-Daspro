import os
import csv
from functions import *
def save(username, store_game, riwayat, kepemilikan):
    jumlah_user = jumlah(username)
    jumlah_game = jumlah(store_game)
    jumlah_riwayat = jumlah(riwayat)
    jumlah_kepemilikan = jumlah(kepemilikan)
    savename = input('Masukkan Nama folder: ')
    try:
        os.mkdir("./"+savename)
    except OSError as e:
        print("Nama Folder sudah ada")

    with open('./'+savename+'data_login.csv','w', newline='') as userfile:
        head = ['user_id','nama','username','password','role','saldo']
        isiuser = csv.DictWriter(userfile,fieldnames=head,delimiter=',')
        for i in range (jumlah_user):
            if i==0 :
                isiuser.writeheader()
            else:
                isiuser.writerow({'user_id':username[i][0], 'nama':username[i][1], 'username':username[i][2], 'password':username[i][3], 'role':username[i][4], 'saldo':username[i][5]})

    with open('./'+savename+'store_game.csv','w', newline='') as gamefile:
        head = ['game_id','nama','kategori','tahun_rilis','harga','stok']
        isigame = csv.DictWriter(gamefile,fieldnames=head,delimiter=',')
        for i in range (jumlah_game):
            if i==0 :
                isigame.writeheader()
            else:
                isigame.writerow({'game_id':store_game[i][0], 'nama':store_game[i][1], 'kategori':store_game[i][2], 'tahun_rilis':store_game[i][3], 'harga':store_game[i][4], 'stok':store_game[i][5]})

    with open('./'+savename+'riwayat.csv','w', newline='') as riwayatfile:
        head = ['user_id','game_id','nama','harga','tahun_beli']
        isiriwayat = csv.DictWriter(riwayatfile,fieldnames=head,delimiter=',')
        for i in range (jumlah_riwayat):
            if i==0 :
                isiriwayat.writeheader()
            else:
                isiriwayat.writerow({'user_id':riwayat[i][0], 'game_id':riwayat[i][1], 'nama':riwayat[i][2], 'harga':riwayat[i][3], 'tahun_beli':riwayat[i][4]})

    with open('./'+savename+'kepemilikan.csv','w', newline='') as kepemilikan_file:
        head = ['game_id','user_id']
        isikepemilikan = csv.DictWriter(kepemilikan_file,fieldnames=head,delimiter=',')
        for i in range (jumlah_kepemilikan):
            if i==0 :
                isikepemilikan.writeheader()
            else:
                isikepemilikan.writerow({'game_id':kepemilikan[i][0], 'user_id':kepemilikan[i][1]})
                
def save_F04 (lines):
    g=open("store_game.csv", 'a')
    g.writelines(lines)
    g.close()
   
def save_F05_F06_ (unChanged_line,Changed_line) :
    g=open("store_game.csv", 'w')
    g.writelines(unChanged_line)
    g.close()
    g=open("store_game.csv", 'a')
    g.writelines(Changed_line)
    g.close()
