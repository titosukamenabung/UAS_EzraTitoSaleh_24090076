class Buah:

    def __init__(self, jenis, warna):
        self.jenis = jenis
        self.warna = warna


    def setjenis(self, item):
        self.jenis = item


    def information(self):
        return f' : {self.jenis} | Warna buah: {self.warna}'

buah1 = Buah('Jambu','Pink','hambar')
buah1.setjenis('kelengkeng')
print(buah1.information())

buah2 = Buah ('salak','putih','manis')
buah2.setjenis('jeruk')
print(buah2.information())