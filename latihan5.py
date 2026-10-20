# Program Analisis Teks Lanjutan menggunakan String, List, Set, dan Dictionary

# Contoh teks sampel untuk dianalisis
teks = """
Belajar pemrograman python sangat menyenangkan dan menantang. 
Python adalah salah satu bahasa pemrogramann yang paling populer di dunia. 
Dengan python, kita bisa membuat berbagai aplikasi mulai dari web, data science, 
hingga kecerdasan buatan. Belajar python membutuhkan ketekunan dan latihan yang konsisten.
Semangat terus dalam belajar python!
"""

# Membersihkan teks dari tanda baca dan mengubahnya menjadi huruf kecil (case-insensitive)
import string
for tanda in string.punctuation:
    teks = teks.replace(tanda, "")
teks_lowercase = teks.lower()

# Memecah teks menjadi list kata-kata
daftar_kata = teks_lowercase.split()
total_kata = len(daftar_kata)

# (a) Menghitung frekuensi setiap kata menggunakan Dictionary
frekuensi_kata = {}
for kata in daftar_kata:
    # Menggunakan metode setdefault atau logika standar dictionary
    frekuensi_kata[kata] = frekuensi_kata.get(kata, 0) + 1

# (b) Menampilkan 10 kata paling sering muncul
# Menggunakan fungsi sorted berdasarkan frekuensi (nilai dictionary) secara descending
kata_teratas = sorted(frekuensi_kata.items(), key=lambda x: x[1], reverse=True)[:10]

# (c) Mengidentifikasi kata yang hanya muncul sekali (hapax legomena)
# Menggunakan list comprehension atau set/dict untuk mencari kata dengan frekuensi == 1
hapax_legomena = [kata for kata, freq in frekuensi_kata.items() if freq == 1]

# (d) Menghitung Type-Token Ratio (TTR)
# Rasio antara jumlah kata unik (set) terhadap total kata keseluruhan
kata_unik = set(daftar_kata)
jumlah_kata_unik = len(kata_unik)
type_token_ratio = jumlah_kata_unik / total_kata if total_kata > 0 else 0

# --- Menampilkan Hasil Output ---
print("=== HASIL ANALISIS TEKS ===")
print(f"Total Kata Keseluruhan : {total_kata}")
print(f"Jumlah Kata Unik       : {jumlah_kata_unik}")
print(f"(d) Type-Token Ratio (TTR): {type_token_ratio:.2f} ({type_token_ratio*100:.1f}%)")

print("\n(a) Frekuensi Kata (Dictionary):")
for kata, freq in frekuensi_kata.items():
    print(f"    - '{kata}': {freq}x")

print("\n(b) 10 Kata Paling Sering Muncul:")
for i, (kata, freq) in enumerate(kata_teratas, 1):
    print(f"    {i}. '{kata}' muncul {freq} kali")

print(f"\n(c) Kata yang Hanya Muncul Sekali (Hapax Legomena) [{len(hapax_legomena)} kata]:")
print(f"    {hapax_legomena}")