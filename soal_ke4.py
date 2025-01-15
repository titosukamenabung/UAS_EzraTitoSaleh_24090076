class Buah:
    def _init_(self):
        self.Nama = ""
        self.Warna = ""
        self.Rasa = ""

    def setNama(self, nama):
        self.Nama = nama

    def setWarna(self, warna):
        self.Warna = warna

    def setRasa(self, rasa):
        self.Rasa = rasa

    def info(self):
        return f"Buah {self.Nama} memiliki warna {self.Warna} dan rasa {self.Rasa}."

kurma = Buah()
kurma.setNama("Kurma")
kurma.setWarna("Coklat")
kurma.setRasa("Manis")
print(kurma.info())