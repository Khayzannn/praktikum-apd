produk = {
    1: {'Diecast': 'Ferrari 499p', 'stok': 2, 'Harga': 330000},
    2: {'Diecast': 'Porsche 963 LMDh', 'stok': 0, 'Harga': 400000},
    3: {'Diecast': 'Ferrari SF-24', 'stok': 0, 'Harga': 140000},
    4: {'Diecast': 'Porsche 911 GT3', 'stok': 5, 'Harga': 100000},
    5: {'Diecast': 'BMW M4 GT3', 'stok': 0, 'Harga': 150000},
    6: {'Diecast': 'BMW M V8 Hybrid', 'stok': 1, 'Harga': 300000},
    7: {'Diecast': 'Mercedes AMG Petronas F1', 'stok': 0, 'Harga': 140000},
    8: {'Diecast': 'McLaren F1', 'stok': 3, 'Harga': 140000},
    9: {'Diecast': 'Lotus 67', 'stok': 0, 'Harga': 40000},
    10: {'Diecast': 'Peugeot 9x8', 'stok': 6, 'Harga': 190000},
    11: {'Diecast': 'Cadillac V-Series R V8', 'stok': 0, 'Harga': 50000}
} #variaabel global

user = {"Attol": {'password': 'adminGanteng67', 'role': 'admin'}}#variaabel global
userLogin = None #variaabel global

def tampilkan_produk_status(stok, nama):
    status = "Ready" if stok > 0 else "Not Ready" #variabel lokal
    print(f"{nama} - {stok} unit ({status})")

def tampilkan_menu_awal():
    print("""
    ===================================
    |  Le Mans Diecast Indonesia      |
    ===================================
    |          1. Registrasi          |
    |          2. Login               |
    |          3. Keluar              |
    ===================================
    """)

def tampilkan_produk():
    for ID, item in produk.items():
        tampilkan_produk_status(item['stok'], item['Diecast'])


def registrasi():
    username = input("Masukkan Nama Anda: ").strip()
    if username in user:
        print("Username sudah tersedia, gunakan nama lain.")
    else:
        password = input("Masukkan Password: ").strip()
        role = input("Masuk sebagai (Admin/Pembeli): ").strip().lower()
        if role in ['admin', 'pembeli']:
            user[username] = {'password': password, 'role': role}
            print(f"Registrasi berhasil! Silakan login dengan username: {username}")
        else:
            print("Role tidak valid.")

def login():
    global userLogin
    username = input("Masukkan Username: ").strip()
    password = input("Masukkan Password: ").strip()
    if username not in user:
        print("Username tidak ditemukan. Silakan registrasi.")
    elif user[username]['password'] != password:
        print("Password salah.")
    else:
        userLogin = {'username': username, 'role': user[username]['role']}
        print(f"Login berhasil sebagai {userLogin['role']}")
        if userLogin['role'] == 'admin':
            menu_admin()
        else:
            menu_pembeli()

def menu_admin():
    while True:
        print("""
=============================
|        Menu Admin         |
=============================
| 1. Lihat Stok Diecast     |
| 2. Tambah Produk          |
| 3. Update Stok            |
| 4. Hapus Produk           |
| 5. Keluar                 |
=============================
""")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tampilkan_produk()
        elif pilihan == "2":
            tambah_produk()
        elif pilihan == "3":
            update_stok()
        elif pilihan == "4":
            hapus_produk()
        elif pilihan == "5":
            print("Keluar dari menu Admin.")
            break
        else:
            print("Pilihan tidak valid.")

def tambah_produk():
    nama = input("Nama produk: ").strip()
    stok = input("Stok: ")
    harga = input("Harga: ")

    if not stok.isdigit() or not harga.isdigit():
        print("Stok dan harga harus berupa angka.")
        return

    stok = int(stok)
    harga = int(harga)
    id_baru = max(produk.keys()) + 1
    produk[id_baru] = {'Diecast': nama, 'stok': stok, 'Harga': harga}
    print(f"Produk {nama} berhasil ditambahkan.")



def update_stok():
    tampilkan_produk()
    id_produk = input("ID produk: ")

    if not id_produk.isdigit() or int(id_produk) not in produk:
        print("ID tidak valid.")
        return

    id_produk = int(id_produk)
    aksi = input("Tambah/Kurangi: ").lower()
    jumlah = input("Jumlah: ")

    if not jumlah.isdigit():
        print("Jumlah harus angka.")
        return

    jumlah = int(jumlah)
    if aksi == "tambah":
        produk[id_produk]['stok'] += jumlah
    elif aksi == "kurangi":
        produk[id_produk]['stok'] = max(0, produk[id_produk]['stok'] - jumlah)
    else:
        print("Aksi tidak valid.")
        return

    print(f"Stok sekarang: {produk[id_produk]['stok']} unit")



def hapus_produk():
    tampilkan_produk()
    hapus = input("Pilih nomor produk yang ingin dihapus: ")
    if hapus.isdigit() and int(hapus) in produk:
        hapus = int(hapus)
        nama = produk[hapus]['Diecast']
        konfirmasi = input(f"Yakin ingin menghapus {nama}? (ya/tidak): ").lower()
        if konfirmasi == "ya":
            produk.pop(hapus)
            print(f"Produk {nama} dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print("ID tidak valid.")

def hitung_total(harga, jumlah):
    return harga * jumlah


def menu_pembeli():
    while True:
        print("""
=============================
|        Menu Pembeli       |
=============================
| 1. Lihat Produk           |
| 2. Beli Produk            |
| 3. Keluar                 |
=============================
""")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tampilkan_produk()
        elif pilihan == "2":
            beli_produk()
        elif pilihan == "3":
            print("Keluar dari menu Pembeli.")
            break
        else:
            print("Pilihan tidak valid.")

def beli_produk():
    tampilkan_produk()
    pilih = input("Pilih ID produk yang ingin dibeli: ")

    if not pilih.isdigit() or int(pilih) not in produk:
        print("ID tidak valid.")
        return

    pilih = int(pilih)
    if produk[pilih]['stok'] == 0:
        print("Produk tidak tersedia.")
        return

    jumlah = input("Masukkan jumlah yang ingin dibeli: ")
    if not jumlah.isdigit():
        print("Jumlah harus angka.")
        return

    jumlah = int(jumlah)
    if jumlah > produk[pilih]['stok']:
        print("Stok tidak mencukupi.")
        return

    total_harga = hitung_total(produk[pilih]['Harga'], jumlah)
    print(f"Total harga: Rp{total_harga:,}")
    konfirmasi = input("Lanjutkan pembelian? (ya/tidak): ").lower()

    if konfirmasi == "ya":
        produk[pilih]['stok'] -= jumlah
        print("Pembelian berhasil!")
    else:
        print("Pembelian dibatalkan.")

print("""
=======================================================
| Selamat Datang di Le Mans Diecast Indonesia         |
| Silahkan lakukan Registrasi atau Login              |
=======================================================
""")

while True:
    tampilkan_menu_awal()
    opsi = input("Pilih Menu: ")
    if opsi == "1":
        registrasi()
    elif opsi == "2":
        login()
    elif opsi == "3":
        print("Terima kasih telah menggunakan layanan kami.")
        break
    else:
        print("Input tidak valid.")