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
}


user = {}
userLogin = None

print("""
     =======================================================
     | Selamat Datang di Le Mans Diecast Indonesia  |
     |         Silahkan lakukan Registrasi          |
     =======================================================
    """)

while True:
    print("""
    ===================================
    |    Le Mans Diecast Indonesia    |
    ===================================
    |          1. Registrasi          |
    |          2. Login               |
    |          3. Keluar              |
    ===================================  """)

    opsi = input('Pilih Menu: ')
    
    if opsi == "1":
        print('== Registrasi pengguna baru ==')
        username = input('Masukkan Nama anda: ').strip()
        
        
        if username in user:
            print('Username sudah tersedia silahkan gunakan nama lain')
        else:
            password = input('Masukkan Password anda: ').strip()
            input_role = input('Anda masuk sebagai: (Admin/Pembeli)').strip().lower()
            if input_role not in ['admin', 'pembeli']:
                print('Input tidak valid')
            else:
                user[username] = {'password': password, 'role': input_role}
                print('Registrasi berhasil. Silahkan Login dengan username: ', username)            

    elif opsi == "2":
        print('=== LOGIN ===')
        username = input('Masukkan Nama pengguna: ').strip()
        password = input('Masukkan password anda: ').strip()

        if username not in user:
            print('''Username tidak ditemukan
            Silahkan Lakukan Registrasi
            ''')
        elif user[username]['password'] != password:
            print('Password salah silahkan coba lagi')
        else:
            userLogin = {'username': username, 'role': user[username]['role']}
            print(f"Login berhasil selamat datang {username} ({userLogin['role']})")
            if userLogin['role'] == 'admin':
                while True:
                    print('''
=============================
|        Menu Admin         |
=============================
| 1. Lihat Stok Diecast     |
| 2. Tambah Diecast Baru    |
| 3. Update Stok Diecast    |
| 4. Hapus Produk Diecast   |
| 5. Keluar                 |
=============================
                ''')
                    pilihanAdmin = input('pilih menu: ')
                    if pilihanAdmin == "1":
                        print('===Daftar Produk dan stok===')
                        for ID, item in produk.items():
                            status = "Ready" if item['stok'] > 0 else "Not Ready"
                            print(f"{ID}. {item['Diecast']} - {item['stok']} unit ({status})")

                    elif pilihanAdmin == '2':
                        print('=== TAMBAH PRODUK BARU ===')
                        namaProduk = input('Nama produk baru: ').strip()
                        jumlahStok = input('Jumlah stok: ').strip()
                        harga = input('Harga produk: ').strip()

                        if jumlahStok.isdigit() and harga.isdigit():
                            jumlahStok = int(jumlahStok)
                            harga = int(harga)
                            ID = max(produk.keys()) + 1 if produk else 1
                            produk[ID] = {'Diecast': namaProduk, 'stok': jumlahStok, 'Harga': harga}
                            print(f"Produk {namaProduk} berhasil ditambahkan dengan ID {ID}, dengan stok {jumlahStok} unit dan harga: {harga}")
                        else:    
                            print("Input stok dan harga harus berupa angka!")

                    elif pilihanAdmin =='3':
                        print('=== UPDATE STOK ===')
                        for ID, item in produk.items():
                            status = "Ready" if item['stok'] > 0 else "Not Ready"
                            print(f"{ID}. {item['Diecast']} - {item['stok']} unit ({status})")
                        pilihProduk =  input('Pilih Nomor produk yang ingin di update: ') 
                        if pilihProduk.isdigit():
                            pilihProduk = int(pilihProduk)
                            action = input('Tambah/Kurangi: ').strip().lower()
                            jumlah = int(input('Berapa jumlahnya: '))
                            if action == "tambah":
                                produk[pilihProduk] ['stok'] += jumlah
                            elif action == 'kurangi':
                                produk[pilihProduk] ['stok'] = max(0, produk[pilihProduk] ['stok'] - jumlah)              
                            print(f"Stok {produk[pilihProduk] ['Diecast']} sekarang adalah {produk[pilihProduk] ['stok']} unit ")
                        else:
                            print('input harus berupa angka')
                    elif pilihanAdmin == '4':
                        print('=== HAPUS PRODUK ===')
                        for ID, item in produk.items():
                            status = "Ready" if item['stok'] > 0 else "Not Ready"
                            print(f"{ID}. {item['Diecast']} - {item['stok']} unit ({status})")
                        hapusDiecast = input('Pilih nomor produk yang ingin dihapus:  ')
                    
                        if hapusDiecast.isdigit():
                            hapusDiecast = int(hapusDiecast) 
                            if hapusDiecast in produk:
                                namaHapus = produk[hapusDiecast]['Diecast']
                                confirm = input('Apakah anda benar benar ingin menghapus produk? (ya/tidak): ').strip().lower()
                                if confirm =='ya':
                                    produk.pop(hapusDiecast)
                                    print(f'Produk {namaHapus} berhasil dihapus')
                                elif confirm == 'tidak':
                                    print(f'Batal menghapus {namaHapus}')
                                else:
                                    print('Jawaban tidak valid')
                        else:
                            print('Input harus berupa angka')
                    elif pilihanAdmin == '5':
                        break
                    else:
                        print('Pilihan tidak valid')
            elif userLogin['role'] == 'pembeli':
                while True:
                    print('''
=============================
|        Menu Pembeli       |
=============================
| 1. Lihat Semua Produk     |
| 2. Beli Produk            |
| 3. Keluar                 |
=============================
                ''') 
                
                    pilihanBuyer = input('Pilih menu: ')
                    if pilihanBuyer == "1": 
                        print('===DAFTAR PRODUK===')
                        for ID, item in produk.items():
                            status = "Ready" if item['stok'] > 0 else "Not Ready"
                            print(f"{ID}. {item['Diecast']} - {item['stok']} unit ({status})")
                    elif pilihanBuyer == "2":
                        print('===DAFTAR PRODUK===')
                        for ID, item in produk.items():
                            status = "Ready" if item['stok'] > 0 else "Not Ready"
                            print(f"{ID}. {item['Diecast']} - {item['stok']} unit ({status})")

                        pilihProduk = input("Pilih produk (input harus dengan angka): ")
                        if not pilihProduk.isdigit():
                            print('Input harus berupa angka')
                        elif int (pilihProduk) not in produk:
                            print('Produk tidak ditemukan')
                        else:
                            IDproduk = int(pilihProduk) 
                            if produk[IDproduk]['stok'] == 0:
                                print('Produk ini sedang kosong atau sedang dalam pengiriman')
                            elif produk[IDproduk]['stok'] > 0:
                                jumlahBeli = input("Jumlah yang ingin dibeli: ")
                                if not jumlahBeli.isdigit():
                                    print('Input harus berupa angka')
                                else:
                                    jumlahBeli = int(jumlahBeli)
                                    if jumlahBeli > produk[IDproduk]['stok']:
                                        print('Jumlah melebihi stok yang tersedia')
                                    else:
                                        produk[IDproduk]['stok'] -= jumlahBeli
                                        totalharga = jumlahBeli * produk [IDproduk] ['Harga']
                                        print(f"Berhasil membeli {jumlahBeli} unit {produk[IDproduk]['Diecast']}")
                                        print(f"Total Harga: Rp {totalharga}")
                                        print(f"Sisa stok: {produk[IDproduk]['stok']} unit")
                    elif pilihanBuyer == "3":
                        print('Terima kasih telah menggunakan layanan kami')
                        break


    elif opsi == "3":
        print('Terima kasih telah menggunakan layanan kami')
        break
    else:
        print('Input tidak valid, silahkan coba lagi')