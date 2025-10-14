# Budi ingin menghitung tagihan listrik bulanannya berdasarkan pemakaian kWh.
# Dengan ketentuan tarif sebagai berikut:
# Jika pemakaian ≤ 100 kWh maka tarif Rp 1.200 per kWh
# Jika pemakaian 101 – 300 kWh maka tarif Rp 1.500 per kWh
# Jika pemakaian > 300 kWh maka tarif Rp 2.000 per kWh
# Rumus: Total Bayar = Pemakaian × Tarif per kWh

pemakaian = int(input("MASUKKAN KWh LISTRIK ANDA"))

total1 = pemakaian * 1200
total2 = pemakaian * 1500
total3 = pemakaian * 2000
if pemakaian <=100 :
    print('total pemakaian', total1)

elif pemakaian <=300:
    print(f'total tagihan anda {total2}')

elif pemakaian > 300:
    print(f'total tagihan anda {total3}')


