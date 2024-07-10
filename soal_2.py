import pandas as pd

data = [
    ["Mahasiswa 1", 90, 80],
    ["Mahasiswa 2", 50, 60],
    ["Mahasiswa 3", 65, 70]
]

df = pd.DataFrame(data, columns=["Nama", "Algoritma dan Struktur Data 2", "Matematika Numerik"])

rata_rata_mk = df[["Algoritma dan Struktur Data 2", "Matematika Numerik"]].mean()
print("Rata-rata nilai untuk setiap mata kuliah:")
print(rata_rata_mk)
print(10*"-")

rata_rata_mahasiswa = df[["Algoritma dan Struktur Data 2", "Matematika Numerik"]].mean(axis=1)
print("Rata-rata nilai untuk setiap mahasiswa:")
print(rata_rata_mahasiswa)