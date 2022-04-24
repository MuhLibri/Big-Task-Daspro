import time, sys
from functions import *
import os

def save(data, data_legend):
    nama_folder = input('Masukkan nama folder penyimpanan: ')
    
    # dapatkan direktori kerja saat ini
    curr_path = os.getcwd()
    list_dirs = []
    isExist = False
    for (_, sub_dirs, _) in os.walk(curr_path):
        list_dirs = Array(list_dirs, sub_dirs)
        break

    # loop melalui list_dirs
    for item in list_dirs:
        if item == nama_folder:
            isExist = True
            break

    # buat dir baru jika tidak ada
    if not isExist:
        os.mkdir(nama_folder)
    defined_dir_path = curr_path + '\\' + nama_folder

    # tulis data ke folder yang ditentukan
    for index in range(panjang(data)):
        temp_file_path = defined_dir_path + '\\' + data_legend[index]
        overwrite(temp_file_path, data[index])

    print('Loading', end='')
    sys.stdout.flush()
    for _ in range(3):
        time.sleep(2)
        print('.', end='')
        sys.stdout.flush()
    print('\nFile berhasil disimpan.')
