def array_2d_nilai():
    jumlah_mahasiswa = 3
    jumlah_mata_kuliah = 2

jumlah_mahasiswa = 3
jumlah_mata_kuliah = 2

nilai_mahasiswa = [
    [90,80],
    [50,60],
    [65,70]
]

rata_rata_mata_kuliah = []
for j in range(jumlah_mata_kuliah):
    total_nilai = 0
    for i in range(jumlah_mahasiswa):
        total_nilai += nilai_mahasiswa[i][j]
    rata_rata_mata_kuliah.append(total_nilai / jumlah_mahasiswa)

rata_rata_mahasiswa = []
for i in range(jumlah_mahasiswa):
    total_nilai = 0
    for j in range(jumlah_mata_kuliah):
        total_nilai += nilai_mahasiswa[i][j]
    rata_rata_mahasiswa.append(total_nilai / jumlah_mata_kuliah)

print("Nilai Mahasiswa:")
for i in range(jumlah_mahasiswa):
    print(f"Mahasiswa {i+1}: {nilai_mahasiswa[i]}")

print("\nRata-rata per Mata Kuliah:")
for i in range(jumlah_mata_kuliah):
    print(f"Mata Kuliah {i+1}: {rata_rata_mata_kuliah[i]}")

print("\nRata-rata per Mahasiswa:")
for i in range(jumlah_mahasiswa):
    print(f"Mahasiswa {i+1}: {rata_rata_mahasiswa[i]}")