class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa
        
    def set_nama(self, nama):
        self.nama = nama
        
    def set_warna(self, warna):
        self.warna = warna

    def set_rasa(self, rasa):
        self.rasa = rasa
    
    def informasi(self):
        return f'Nama buah: {self.nama}\nWarna : {self.warna}\nRasa : {self.rasa}'    
    
class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        Buah.__init__(self, nama, warna, rasa)
        self.vitamin = vitamin
    
    def set_vitamin(self, vitamin):
        self.__ukuran_file = vitamin
    
    def information(self):
        return f'{self.informasi()}\nVitamin : {self.vitamin}'