print("Pilih operasi yang diinginkan:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Pengalian")
print("4. Pembagian")

pilihan = input("pilih operasi = (1/2/3/4): ")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == '1':
    hasil = angka1 + angka2
elif pilihan == '2':
    hasil = angka1 - angka2
elif pilihan == '3':
    hasil = angka1 * angka2
elif pilihan == '4':
    hasil = angka1 / angka2
else:
    print("Pilihan tidak ada")
print("Hasil:", hasil)