nama_barang = input("Masukkan nama barang: ")
harga = int(input("Masukkan harga barang: "))
jumlah = int(input("Masukkan jumlah barang: "))

total = harga * jumlah

print("\n===== STRUK PEMBELIAN =====")
print("Barang  :", nama_barang)
print("Harga   : Rp", harga)
print("Jumlah  :", jumlah)
print("--------------------------")
print("TOTAL   : Rp", total)
print("==========================")
print("Terima kasih sudah belanja!")