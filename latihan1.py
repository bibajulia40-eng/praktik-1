# Menerima input kalimat dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# (a) Menghitung jumlah kata
# Menggunakan method split() untuk memecah kalimat berdasarkan spasi menjadi list kata[span_2](start_span)[span_2](end_span)[span_3](start_span)[span_3](end_span)
daftar_kata = kalimat.split()
jumlah_kata = len(daftar_kata)

# (b) Menghitung jumlah karakter (termasuk spasi)
jumlah_karakter = len(kalimat)

# (c) Menampilkan kata terpanjang
# Menggunakan fungsi max dengan parameter key=len untuk mencari kata dengan panjang maksimum
if jumlah_kata > 0:
    kata_terpanjang = max(daftar_kata, key=len)
else:
    kata_terpanjang = ""

# (d) Menampilkan kalimat dengan format title case (setiap awal kata huruf kapital)
# Bisa menggunakan method title() bawaan Python[span_4](start_span)[span_4](end_span)[span_5](start_span)[span_5](end_span)
kalimat_title = kalimat.title()

# Menampilkan hasil output ke layar menggunakan f-string[span_6](start_span)[span_6](end_span)[span_7](start_span)[span_7](end_span)
print("\n--- Hasil Analisis Kalimat ---")
print(f"Kalimat asli        : {kalimat}")
print(f"(a) Jumlah kata     : {jumlah_kata}")
print(f"(b) Jumlah karakter : {jumlah_karakter}")
print(f"(c) Kata terpanjang   : {kata_terpanjang}")
print(f"(d) Title case      : {kalimat_title}")