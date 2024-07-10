class AntrianPesanan:
    def __init__(self):
        self.antrian = []

    def tambah_pesanan(self, pesanan):
        self.antrian.append(pesanan)
        print(f"Pesanan {pesanan} ditambahkan ke antrian.")

    def proses_pesanan(self):
        if not self.antrian:
            print("Antrian kosong. Tidak ada pesanan untuk diproses.")
            return None
        pesanan = self.antrian.pop(0)
        print(f"Pesanan {pesanan} diproses.")
        return pesanan

    def tampilkan_antrian(self):
        print("Antrian saat ini: ")
        for i, pesanan in enumerate(self.antrian):
            print(f"{i+1}. {pesanan}")

