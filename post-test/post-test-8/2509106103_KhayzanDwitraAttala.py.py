from autentikasi import registrasi, login

def tampilkan_menu_awal():
    print("""
===================================
|  Le Mans Diecast Indonesia      |
===================================
| 1. Registrasi                   |
| 2. Login                        |
| 3. Keluar                       |
===================================
""")

print("Selamat datang di Le Mans Diecast Indonesia")

while True:
    tampilkan_menu_awal()
    opsi = input("Pilih menu: ")
    if opsi == "1":
        registrasi()
    elif opsi == "2":
        login()
    elif opsi == "3":
        print("Terima kasih telah menggunakan layanan kami.")
        break
    else:
        print("Input tidak valid.")

