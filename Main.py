# Saat pertama kali dijalankan, user hanya dapat melakukan login. User baru bisa mengakses fungsi lain setelah berhasil login. 
# Setelah berhasil login, user akan diarahkan ke menu utama

from Menu import *

(username,password,role) = login()
mainMenu(role,username)