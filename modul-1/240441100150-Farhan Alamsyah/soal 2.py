class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat
    
    def tampilkan_info(self):
        print("\nInformasi Mahasiswa:")
        print(f"Nama    : {self.nama}")
        print(f"NIM     : {self.nim}")
        print(f"Jurusan : {self.jurusan}")
        print(f"Alamat  : {self.alamat}\n")

def input_data_mahasiswa(nomor):
    print(f"Masukkan data mahasiswa ke-{nomor}")
    nama = input("Nama    : ")
    nim = input("NIM     : ")
    jurusan = input("Jurusan : ")
    alamat = input("Alamat  : ")
    print()
    return Mahasiswa(nama, nim, jurusan, alamat)

print("-" * 40)
mahasiswa1 = input_data_mahasiswa(1)
mahasiswa2 = input_data_mahasiswa(2)
mahasiswa3 = input_data_mahasiswa(3)

print("=" * 40)
mahasiswa1.tampilkan_info()
mahasiswa2.tampilkan_info()
mahasiswa3.tampilkan_info()
print("=" * 40)