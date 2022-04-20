# B02 - Magic Conch Shell
import time
from functions import *

def B02():
    print("Kerang Ajaib")
    faktor_random = time.localtime().tm_sec + time.localtime().tm_min + time.localtime().tm_hour
    pertanyaan = input("Apa pertanyaanmu? ")
    jawaban = random(pertanyaan,faktor_random)

    if (jawaban == 1):
        print("Ya")
    elif (jawaban == 2):
        print("YES! YES! YES!")
    elif (jawaban == 3):
        print("NO! NO! NO!")
    elif (jawaban == 4):
        print("Tidak")
    elif (jawaban == 5):
        print("Teruslah bermimpi")
    elif (jawaban == 6):
        print("Anda belum beruntung")
    elif (jawaban == 7):
        print("Coba lagi")
    elif (jawaban == 8):
        print("Pasti dong")
    elif (jawaban == 9):
        print("Sadar diri dong")
    elif (jawaban == 10):
        print("Jika Tuhan berkehendak")
    elif (jawaban == 11):
        print("mungkin")
    elif (jawaban == 12):
        print("bisa jadi")
    return