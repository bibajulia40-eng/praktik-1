# Program Pengolahan Nilai Mahasiswa

# Contoh data list nilai mahasiswa (bisa diubah sesuai keinginan)
nilai_mahasiswa = [85, 92, 78, 65, 90, 55, 70, 88, 40, 95]

print(f"Daftar Nilai Mahasiswa: {nilai_mahasiswa}")

# (a) Menghitung rata-rata nilai
# Menggunakan fungsi sum() untuk total nilai dibagi dengan len() jumlah mahasiswa
total_nilai = sum(nilai_mahasiswa)
jumlah_mhs = len(nilai_mahasiswa)
rata_rata = total_nilai / jumlah_mhs

# (b) Menentukan nilai tertinggi dan terendah menggunakan max() dan min()
nilai_tertinggi = max(nilai_mahasiswa)
nilai_terendah = min(nilai_mahasiswa)

# (c & d) Mengelompokkan kategori nilai dan menghitung frekuensinya menggunakan Dictionary
# Aturan kategori: A (>=85), B (>=70), C (>=55), D (>=40), E (<40)
frekuensi_kategori = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

for nilai in nilai_mahasiswa:
    if nilai >= 85:
        frekuensi_kategori["A"] += 1
    elif nilai >= 70:
        frekuensi_kategori["B"] += 1
    elif nilai >= 55:
        frekuensi_kategori["C"] += 1
    elif nilai >= 40:
        frekuensi_kategori["D"] += 1
    else:
        frekuensi_kategori["E"] += 1

# Menampilkan hasil output
print("\n--- Hasil Analisis Nilai Mahasiswa ---")
print(f"(a) Rata-rata nilai     : {rata_rata:.2f}")
print(f"(b) Nilai Tertinggi     : {nilai_tertinggi}")
print(f"    Nilai Terendah      : {nilai_terendah}")
print(f"(c & d) Frekuensi Kategori (Dictionary):")
for kategori, jumlah in frekuensi_kategori.items():
    print(f"    Kategori {kategori}          : {jumlah} orang")