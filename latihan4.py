# Program Inventaris Toko menggunakan Dictionary dan Tuple

# Dictionary inventaris: kunci = nama barang, nilai = (harga, stok)
inventaris = {
    "Buku Tulis": (5000, 50),
    "Pulpen": (3000, 100),
    "Buku Gambar": (8000, 30),
    "Penghapus": (2000, 75),
    "Penggaris": (4000, 40)
}

print("=== Data Inventaris Awal ===")
for barang, data in inventaris.items():
    print(f"- {barang}: Harga = Rp {data[0]}, Stok = {data[1]}")

# (a) Fungsi untuk menambah barang baru
def tambah_barang(nama, harga, stok):
    if nama in inventaris:
        print(f"\nBarang '{nama}' sudah ada di inventaris!")
    else:
        inventaris[nama] = (harga, stok)
        print(f"\nBerhasil menambah barang baru: {nama} (Harga: Rp {harga}, Stok: {stok})")

# (b) Fungsi untuk mengupdate stok barang
def update_stok(nama, stok_baru):
    if nama in inventaris:
        harga_lama = inventaris[nama][0]
        inventaris[nama] = (harga_lama, stok_baru)
        print(f"\nStok '{nama}' berhasil di-update menjadi: {stok_baru}")
    else:
        print(f"\nBarang '{nama}' tidak ditemukan di inventaris!")

# (c) Fungsi untuk mencari barang berdasarkan rentang harga
def cari_berdasarkan_harga(min_harga, max_harga):
    print(f"\n(c) Barang dengan rentang harga Rp {min_harga} - Rp {max_harga}:")
    ditemukan = False
    for barang, data in inventaris.items():
        harga = data[0]
        if min_harga <= harga <= max_harga:
            print(f"    -> {barang} (Rp {harga}, Stok: {data[1]})")
            ditemukan = True
    if not ditemukan:
        print("    Tidak ada barang dalam rentang harga tersebut.")

# (d) Fungsi untuk menghitung total nilai inventaris (Harga * Stok)
def hitung_total_nilai():
    total_nilai = 0
    for barang, data in inventaris.items():
        harga, stok = data
        total_nilai += (harga * stok)
    return total_nilai

# --- Menguji Fungsi-Fungsi ---
# 1. Tambah barang baru
tambah_barang("Spidol", 6000, 25)

# 2. Update stok barang
update_stok("Pulpen", 120)

# 3. Cari barang dengan harga antara Rp 3000 sampai Rp 7000
cari_berdasarkan_harga(3000, 7000)

# 4. Hitung total nilai inventaris keseluruhan
total_inventaris = hitung_total_nilai()
print(f"\n(d) Total Nilai Keseluruhan Inventaris: Rp {total_inventaris:,}")