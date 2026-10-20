# Program Operasi Set untuk Penerima Beasiswa

# Data ID Mahasiswa penerima Beasiswa A dan Beasiswa B (dalam bentuk list, lalu dikonversi ke set)
beasiswa_a = {"MHS001", "MHS002", "MHS003", "MHS004", "MHS005"}
beasiswa_b = {"MHS003", "MHS004", "MHS006", "MHS007"}

print(f"Penerima Beasiswa A: {beasiswa_a}")
print(f"Penerima Beasiswa B: {beasiswa_b}")

# (a) Mahasiswa yang menerima kedua beasiswa (Irisan / Intersection)[span_2](start_span)[span_2](end_span)[span_3](start_span)[span_3](end_span)[span_4](start_span)[span_4](end_span)
keduanya = beasiswa_a & beasiswa_b # atau menggunakan beasiswa_a.intersection(beasiswa_b)

# (b) Mahasiswa yang hanya menerima beasiswa A (Selisih / Difference A - B)[span_5](start_span)[span_5](end_span)[span_6](start_span)[span_6](end_span)
hanya_a = beasiswa_a - beasiswa_b # atau menggunakan beasiswa_a.difference(beasiswa_b)

# (c) Mahasiswa yang menerima beasiswa B tapi tidak A (Selisih / Difference B - A)[span_7](start_span)[span_7](end_span)[span_8](start_span)[span_8](end_span)
hanya_b = beasiswa_b - beasiswa_a

# (d) Semua mahasiswa unik yang menerima beasiswa (Gabungan / Union)[span_9](start_span)[span_9](end_span)[span_10](start_span)[span_10](end_span)[span_11](start_span)[span_11](end_span)
semua_unik = beasiswa_a | beasiswa_b # atau menggunakan beasiswa_a.union(beasiswa_b)

# Menampilkan hasil output
print("\n--- Hasil Analisis Beasiswa (Operasi Set) ---")
print(f"(a) Penerima kedua beasiswa     : {keduanya}")
print(f"(b) Hanya menerima beasiswa A   : {hanya_a}")
print(f"(c) Hanya menerima beasiswa B   : {hanya_b}")
print(f"(d) Semua mahasiswa unik        : {semua_unik}")