#MEMASUKKAN NAMA DAN NIM
NamaLengkap = str(input('Masukkan Nama Lengkap Anda: '))
NIM = int(input('Masukkan NIM anda: '))
print('\t| Nama: ', NamaLengkap)
print('\t| NIM: ', NIM)

#MENENTUKAN HARGA LAPTOP DAN OUTPUT SESUAI HARGA YANG KITA TENTUKAN
hargalaptop = int(input('MASUKKAN HARGA LAPTOP YANG INGIN ANDA BELI: '))
print(f"{NamaLengkap} dengan NIM {NIM}, Ingin membeli laptop dengan harga Rp.{hargalaptop} ")

#MENGHITUNG DISKON HARGA LAPTOP
HargaLenovo = hargalaptop - (hargalaptop *0.10)
HargaAsus = hargalaptop - (hargalaptop*0.07)
HargaAcer = hargalaptop - (hargalaptop*0.05)

#MENAMPILKAN HARGA SETELAH DISKON
print(f'\n Atas nama {NamaLengkap} dengan NIM {NIM} ingin membeli laptop dengan harga yang sudah ditentukan yaitu {hargalaptop}')
print(f'Jika anda ingin membeli laptop Acer anda harus membayar {HargaAcer} setelah diskon 5%')
print(f'Jika anda ingin membeli laptop Asus anda harus membayar {HargaAsus} setelah diskon 7%')
print(f'Jika anda ingin membeli laptop Lenovo anda harus membayar {HargaLenovo} setelah diskon 10%')