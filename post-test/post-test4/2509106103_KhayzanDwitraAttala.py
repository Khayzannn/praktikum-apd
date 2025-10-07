#LOGIN
print('| Selamat Datang di XXO, Silahkan memasukkan Nama dan NIM anda')

fixedName = "Attala"
fixedNIM = "2509106103"

#variable attempt 
percobaan = 0
max = 3
while percobaan < max:
    
    NamaAja = input('Masukkan Nama Anda: ')
    NIM = (input('Masukkan NIM anda: '))
    if not NIM.isdigit():
        print('NIM Harus berupa angka')
        percobaan += 1
        continue

    elif NamaAja == fixedName and  NIM == fixedNIM:
        percobaan = max
        print(f'Selamat datang {NamaAja} silahkan pilih tiket')
        
        break  
    #jika gagal program akan berhenti
    else:
        percobaan += 1
        sisapercobaan = max - percobaan
        if sisapercobaan > 0:
            print(f'Login gagal silahkan coba lagi')
        else:
            print('Login telah mencapai batas maksimal coba lagi nanti')
            exit()

#list harga dan kategori tiket
print('\t----- HARGA TIKET -----')
print('-------------------------------------------')
print('\t |   Reguler : Rp. 50.000')
print('\t |   VIP : Rp. 100.000')
print('\t |   VVIP : Rp. 150.000')
print('\t |   Keluar')
print('*Harga Per Tiket')
print('--------------------------------------------')

#desicion making ya
pilihan = str(input('\napakah anda ingin melanjutkan?(ya/tidak) ')) .lower()
if pilihan == "ya":
    
    
    #input jumlah
    JumlahTiketReguler = int(input('Berapa tiket Reguler yang ingin anda beli? (input harus berupa angka)'))
    JumlahTiketVIP = int(input('Berapa tiket VIP yang ingin anda beli? (input harus berupa angka) '))
    JumlahTiketVVIP = int(input('Berapa tiket VVIP yang ingin anda beli? (input harus berupa angka) '))

    #variable harga tiket
    Reguler = 50000
    VIP = 100000
    VVIP = 150000
    totalprice = 0
    totaltiket = 0 

    #menghitung menggunakan for
    for i in range(3):
        if i == 0:
            totalReguler = JumlahTiketReguler * Reguler
            totalprice += totalReguler
            totaltiket += JumlahTiketReguler
            print('----------------------------')
            print(f'\t| Subtotal Reguler: {totalReguler}')
        elif i == 1:
            totalVIP = JumlahTiketVIP*VIP
            totalprice += totalVIP
            totaltiket+= JumlahTiketVIP
            print(f'\t| Subtotal VIP: {totalVIP}')
        elif i == 2:
            totalVVIP = JumlahTiketVVIP*VVIP
            totalprice += totalVVIP
            totaltiket += JumlahTiketVVIP
            print(f'\t| Subtotal VVIP: {totalVVIP}')
            print('-----------------------------')
    #diskon
    diskon12 = totalprice-(totalprice*0.12)
    diskon8 = totalprice-(totalprice*0.08)

    #output harga dengan diskon atau tanpa diskon
    if totalprice >= 300000:
        print(f'Total pembelian anda mencapai Rp. 300.000, anda mendapat diskon 12% harga keseluruhan adalah Rp. {diskon12}')
    elif totalprice <300000 and totalprice >=200000:
        print(f'Total pembelian anda mencapai Rp.200.000 anda mendapat diskon 8% harga keseluruhan adalah Rp. {diskon8}')
    elif totalprice <200000 and totalprice >=150000:
        print(f'Total pembelian anda mencapai Rp.150.000 Anda mendapatkan poster Eksklusif harga keseluruhan adalah Rp. {totalprice}') 
    else:
        print(f'Total harga adalah Rp. {totalprice}')


    print('Terimakasih telah menggunakan layanan kami')

    #decision making tidak/tidak valid
elif pilihan == "tidak":
    print('Terima kasih telah menggunakan layanan kami,')
else:
    print('Jawaban Tidak Valid')