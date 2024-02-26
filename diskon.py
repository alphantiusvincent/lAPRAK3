pembelian = int(input("masukkan jumlah pembeliana anda : "))

if pembelian > 1000000:
    diskon = 0.3 # diskon 30%
    print("diskon 30 %")
elif pembelian > 500000 and pembelian <= 1000000:
    diskon = 0.2 # diskon 20%
    print("diskon 20 %")
elif pembelian >= 100000 and pembelian <= 500000:
    diskon = 0.15 # diskon 15%
    print("diskon 15 %")
else:
    diskon = 0 # tidak ada diskon
    
bayar = pembelian - (pembelian * diskon)
print("jadi anda perlu membayar : ", bayar)
 
