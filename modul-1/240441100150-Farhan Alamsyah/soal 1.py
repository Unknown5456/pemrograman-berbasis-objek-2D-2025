class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
    
    def activity(self, kegiatan):
        print("-" * 40)
        print(f"nama: {self.nama}\numur: {self.umur} \nalamat: {self.alamat} \ndia sedang {kegiatan}")

orang1 = Manusia("Wileno", 20, "Jakarta")
orang2 = Manusia("Budi", 19, "Bandung")
orang3 = Manusia("Wowo", 22, "Surabaya")
orang4 = Manusia("Tomas", 105, "Yogyakarta")
orang5 = Manusia("Adit", 97, "Medan")

orang1.activity("berjalan")
orang2.activity("berjalan") 
orang3.activity("berlari")
orang4.activity("berjalan")
orang5.activity("berlari")
print("-" * 40)