def load(name_folder):
    user_file = reader('./'+name_folder+'/data_login.csv')
    riwayat_file = reader('./'+name_folder+'/riwayat.csv')
    game_file = reader('./'+name_folder+'/store_game.csv')
    kepemilikan_file = reader('./'+name_folder+'/kepemilikan.csv')
    return user_file,riwayat_file,game_file,kepemilikan_file