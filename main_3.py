from soal_3 import  AntrianPesanan

antrian = AntrianPesanan()
antrian.tambah_pesanan("Nasi Goreng")
antrian.tambah_pesanan("Ketoprak")
antrian.tambah_pesanan("Lengko")
antrian.tambah_pesanan("Soto")

antrian.tampilkan_antrian()

antrian.proses_pesanan()
antrian.proses_pesanan()

antrian.tampilkan_antrian()

antrian.tambah_pesanan("Mie Ayam")
antrian.tambah_pesanan("Ayam Goreng")

antrian.tampilkan_antrian()

while antrian.antrian:
    antrian.proses_pesanan()
    antrian.tampilkan_antrian()
