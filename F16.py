import os

def save(user, game, riwayat, kepemilikan):
    jumlah_user = jumlah(user)
    jumlah_game = jumlah(game)
    jumlah_riwayat = jumlah(riwayat)
    jumlah_kepemilikan = jumlah(kepemilikan)
    save_name = input('Masukkan Nama folder: ')
    try:
        os.mkdir("./"+save_name)
    except OSError as e:
        print("Nama Folder sudah ada")

    with open('./'+save_name+'data_login.csv','w', newline='') as user_file:
        head = ['user_id','username','nama','password','role','saldo']
        isi_user = csv.DictWriter(user_file,fieldnames=head,delimiter=';')
        for i in range (jumlah_user):
            if i==0 :
                isi_user.writeheader()
            else:
                isi_user.writerow({'user_id':user[i][0], 'username':user[i][1], 'nama':user[i][2], 'password':user[i][3], 'role':user[i][4], 'saldo':user[i][5]})

    with open('./'+save_name+'store_game.csv','w', newline='') as game_file:
        head = ['id','nama','kategori','tahun rilis','harga','stok']
        isi_game = csv.DictWriter(game_file,fieldnames=head,delimiter=';')
        for i in range (jumlah_game):
            if i==0 :
                isi_game.writeheader()
            else:
                isi_game.writerow({'id':game[i][0], 'nama':game[i][1], 'kategori':game[i][2], 'tahun rilis':game[i][3], 'harga':game[i][4], 'stok':game[i][5]})

    with open('./'+save_name+'/riwayat.csv','w', newline='') as riwayat_file:
        head = ['game_id','nama','harga','user_id','tahun beli']
        isi_riwayat = csv.DictWriter(riwayat_file,fieldnames=head,delimiter=';')
        for i in range (jumlah_riwayat):
            if i==0 :
                isi_riwayat.writeheader()
            else:
                isi_riwayat.writerow({'game_id':riwayat[i][0], 'nama':riwayat[i][1], 'harga':riwayat[i][2], 'user_id':riwayat[i][3], 'tahun_beli':riwayat[i][4]})

    with open('./'+save_name+'kepemilikan.csv','w', newline='') as kepemilikan_file:
        head = ['game_id','user_id']
        isi_kepemilikan = csv.DictWriter(kepemilikan_file,fieldnames=head,delimiter=';')
        for i in range (jumlah_kepemilikan):
            if i==0 :
                isi_kepemilikan.writeheader()
            else:
                isi_kepemilikan.writerow({'game_id':kepemilikan[i][0], 'user_id':kepemilikan[i][1]})