mahasiswa = []

while True:
    nim = int(input("Masukkan NIM mahasiswa: "))
    nama = input("Masukan Nama Mahasiswa: ")

    mahasiswa.append({"nim": nim, "nama": nama})

    tambah = input("Apakah Anda ingin menambahkan mahasiswa lagi? (y/t): ")

    if tambah.lower()!= "y":
        break

print("Data Mahasiswa:")
for mahasiswa in mahasiswa:
    print(f"Nama: {mahasiswa['nama']}, NIM: {mahasiswa['nim']}")