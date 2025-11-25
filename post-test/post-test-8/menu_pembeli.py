from data import produk
from menu_admin import tampilkan_produk

def hitung_total(harga, jumlah):
    return harga * jumlah

def menu_pembeli():
    while True:
        print("""
=== Menu Pembeli ===
1. Lihat Produk
2. Beli Produk
3. Keluar
""")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tampilkan_produk()
        elif pilihan == "2":
            beli_produk()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid.")

def beli_produk():
    tampilkan_produk()
    ID = input("ID produk: ")
    if not ID.isdigit() or int(ID) not in produk:
        print("ID tidak valid.")
        return
    ID = int(ID)
    if produk[ID]['stok'] == 0:
        print("Produk tidak tersedia.")
        return
    jumlah = input("Jumlah beli: ")
    if not jumlah.isdigit():
        print("Jumlah harus angka.")
        return
    jumlah = int(jumlah)
    if jumlah > produk[ID]['stok']:
        print("Stok tidak cukup.")
        return
    total = hitung_total(produk[ID]['Harga'], jumlah)
    print(f"Total harga: Rp{total:,}")
    konfirmasi = input("Lanjutkan pembelian? (ya/tidak): ").lower()
    if konfirmasi == "ya":
        produk[ID]['stok'] -= jumlah
        print("Pembelian berhasil.")
    else:
        print("Pembelian dibatalkan.")

