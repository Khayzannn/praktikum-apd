produk = [
    ['Diecast Ferrari 499p',  2, 330000], 
    ['Diecast Porsche 963 LMDh', 0, 400000],
    ['Diecast Ferrari SF-24', 0, 140000],
    ['Diecast Porsche 911 GT3', 5, 100000],
    ['Diecast BMW M4 GT3', 0, 150000],
    ['Diecast BMW M V8 Hybrid', 1, 300000],
    ['Diecast Mercedes AMG Petronas F1', 0, 140000],
    ['Diecast McLaren F1', 3, 140000],
    ['Diecast Lotus 67', 0, 40000],
    ['Diecast Peugeot 9x8', 6, 190000],
    ['Diecast Cadillac V- Series V8', 0, 50000]
]
user = []
registation = []
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
    |  Pembelian Diecast Motorsporst |
    ===================================
    |          1. Registrasi          |
    |          2. Login               |
    |          3. Keluar              |
    ===================================  """)

    opsi = input('Pilih Menu: ')
    if not opsi.isdigit():
        print('Input harus berupa angka')
        continue
    
    elif opsi == "1":
        print('== Registrasi pengguna baru ==')
        username = input('Masukkan Nama anda: ')
        password = input('Masukkan Password anda: ')

        
        
        input_role = input('Anda masuk sebagai: (Admin/Pembeli)').strip().lower()
        if input_role == "admin":
            role = "admin"
        elif input_role == "pembeli":
            role = "pembeli"
        else:
            print('Pilihan Tidak Valid')
            continue

        penggunaTerdaftar = False
        for data_user in user:
            if data_user["username"] == username and data_user["password"] == password:
                penggunaTerdaftar = True
                break 

        if penggunaTerdaftar:
            print("Nama sudah terdaftar, silahkan gunakan nama lain")
        else:
            user.append({"username": username, "password": password, "role": role})
            print('Registrasi berhasil silahkan login')
            
            

    elif opsi == "2":
        if len(user)== 0:
            print('Pengguna tidak ditemukan, silahkan lakukan registrasi')
            continue
        username = input('Masukkan Nama pengguna: ')
        password = input('Masukkan password anda: ')

        userwasfound = False
        for data_user in user:
            if data_user["username"] == username and data_user["password"] == password:
                userLogin = data_user
                userwasfound = True
                break
        if not userwasfound        :
            print('Nama pengguna atau kata sandi salah')
            continue
        
        elif userLogin["role"].lower() == 'admin':
            while True:
                print('''
=============================
|        Menu Admin         |
=============================
| 1. Lihat Stok Diecast     |
| 2. Tambah Diecast Baru   |
| 3. Update Stok Diecast   |
| 4. Hapus Produk Diecast    |
| 5. Keluar                 |
=============================
                    ''')
                pilihanAdmin = input('pilih menu: ')
                if pilihanAdmin == "1":
                    print('Daftar Produk dan stok')
                    
                    i= 1
                    for item in produk:
                        nama = item[0]
                        stok = item[1]
                        status = "Ready" if stok > 0 else "Not Ready"
                        print(f'{i}. {nama} - {stok} unit {status}')
                        i +=1
                elif pilihanAdmin == '2':
                    
                    print('=== TAMBAH PRODUK BARU ===')
                    namaProduk = input('Nama produk baru: ').strip()
                    jumlahStok = input('Jumlah stok: ').strip()
                    harga = input('Harga produk: ').strip()

    
                    if jumlahStok.isdigit() and harga.isdigit():
                        jumlahStok = int(jumlahStok)
                        harga = int(harga)

      
                        ada = False
                        for item in produk:
                            if item[0].lower() == namaProduk.lower():
                                ada = True
                                break

                        if ada:
                            print(f"Produk {namaProduk} sudah ada. Gunakan menu update stok.")
                        else:
                            produk.append([namaProduk, jumlahStok, harga])
                            print(f"Produk {namaProduk} berhasil ditambahkan dengan stok {jumlahStok} unit dan harga Rp{harga:,}")
                    else:
                        print("Input stok dan harga harus berupa angka!")



                elif pilihanAdmin =='3':
                    print('===DAFTAR PRODUK===')
                    i = 1
                    for item in produk:
                        print(f'{i}. {item[0]} - {item[1]} unit')
                        i+=1
                    pilihProduk =  input('Pilih Nomor produk: ')
                    
                    if pilihProduk.isdigit():
                        indexList = int(pilihProduk) -1
                        if 0 <= indexList < len(produk):
                            namaProduk = produk[indexList] [0]

                            action = input('Tambah/Kurangi: ').strip().lower()
                            jumlah = int(input('Berapa jumlahnya: '))
                            if action == "tambah":
                                produk[indexList] [1] += jumlah
                            elif action == 'kurangi':
                                produk[indexList] [1] -= jumlah

                                if produk[indexList] [1] < 0:
                                    produk[indexList] [1] = 0
                            print(f'stok {namaProduk} sekarang adalah {produk[indexList] [1]} unit')
                    else:
                        print('input harus berupa angka')
                elif pilihanAdmin == '4':
                    print('Daftar Produk dan stok')
                    
                    i= 1
                    for item in produk:
                        nama = item[0]
                        stok = item[1]
                        status = "Ready" if stok > 0 else "Not Ready"
                        print(f'{i}. {nama} - {stok} unit {status}')
                        i +=1
                    hapusDiecast = input('Pilih nomor produk yang ingin dihapus:  ')
                    if hapusDiecast.isdigit():
                        hapusDiecast = int(hapusDiecast) -1
                        if 0 <= hapusDiecast < len(produk):
                            namaProduk
                            confirm = input('Apakah anda benar benar ingin menghapus produk? (ya/tidak): ').strip().lower()
                            if confirm =='ya':
                                produk.pop(hapusDiecast)
                                print('Produk berhasil dihapus')
                            elif confirm == 'tidak':
                                print(f'Batal menghapus {namaProduk}')
                            else:
                                print('Jawaban tidak valid')
                    
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
                    i = 1
                    print('===DAFTAR PRODUK===')
                    for item in produk:
                        status = 'Ready' if item[1] > 0 else "Not Ready"
                        print(f'{i}. {item[0]} - {item[1]} unit ({status}) - Rp {item[2]:,}')
                        i+=1
                elif pilihanBuyer == "2":
                    i = 1
                    for item in produk:
                        status = 'Ready' if item[1] > 0 else "Not Ready"
                        print(f"{i}. {item[0]} - {item[1]} unit ({status}) - Rp{item[2]:,}")
                        i += 1

                    pilihProduk = input("Pilih produk (input harus dengan angka): ")

                    if pilihProduk.isdigit():
                        indexProduk = int(pilihProduk) - 1   # -1 karena list mulai dari 0
                        if 0 <= indexProduk < len(produk):
                            if produk[indexProduk][1] > 0:
                                jumlahBeli = int(input("Jumlah yang ingin dibeli: "))
                                if jumlahBeli <= produk[indexProduk][1]:
                                    produk[indexProduk][1] -= jumlahBeli
                                    total = jumlahBeli * produk[indexProduk][2]
                                    print(f"{jumlahBeli} unit {produk[indexProduk][0]} berhasil dibeli. Total Rp{total:,}")
                                else:
                                    print("Stok tidak mencukupi!")
                            else:
                                print("Produk tidak tersedia!")
                        else:
                            print("Nomor produk tidak valid!")
                    else:
                        print("Input harus berupa angka!")

                elif pilihanBuyer == "3":
                    break


    elif opsi == "3":
        print('Terima kasih telah menggunakan layanan kami')       