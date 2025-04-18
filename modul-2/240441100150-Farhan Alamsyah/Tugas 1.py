class Mahasiswa:  
    total_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.daftar_matkul = []
        self.validasi_nim = self.validasi_nim(nim)
        Mahasiswa.total_mahasiswa += 1 

    def tampilkan_info(self): 
        print("\n" + "=" * 60)
        print(f"NAMA\t: {self.nama.upper()}")
        print(f"NIM\t: {self.nim} {'(TIDAK VALID)' if not self.validasi_nim else ''}")
        print(f"PRODI\t: {self.prodi.upper()}")
        print("\nMATA KULIAH YANG DIAMBIL:")
        for i, matkul in enumerate(self.daftar_matkul, 1):
            status = " (SKS TIDAK VALID)" if not matkul.validasi_sks(matkul.sks) else ""
            print(f"{i}. {matkul.nama} - {matkul.sks} SKS{status}")
        print("=" * 60)

    def tambah_matkul(self, matkul):
        self.daftar_matkul.append(matkul)

    @classmethod
    def jumlah_mahasiswa(cls):
        print(f"\nTOTAL MAHASISWA: {cls.total_mahasiswa}")

    @staticmethod
    def validasi_nim(nim):
        nim_str = str(nim)
        return len(nim_str) == 10 and nim_str.startswith('23') 


class MataKuliah:  
    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks  

    @staticmethod
    def validasi_sks(sks):
        return sks in {2, 3}


class Kampus:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        self.nama_valid = self.validasi_nama(nama)

    def tampilkan_info(self):
        print("\n" + "=" * 60)
        print("INFORMASI KAMPUS".center(60))
        print("=" * 60)
        print(f"Nama\t: {self.nama}{' (TIDAK VALID)' if not self.nama_valid else ''}")
        print(f"Alamat\t: {self.alamat}")
        print("=" * 60)

    @staticmethod
    def validasi_nama(nama):
        for char in nama:
            if not (char.isalpha() or char.isspace()):
                return False
        return True


daftar_matkul = [
    MataKuliah("MK001", "Pemrograman Berbasis Objek", 3),
    MataKuliah("MK002", "Pengantar Basis Data", 3),
    MataKuliah("MK003", "Algoritma Pemograman", 3),
    MataKuliah("MK004", "Analisa Proses Bisnis", 2),
    MataKuliah("MK005", "Bahasa Inggris", 2),
    MataKuliah("MK006", "Logika Engineering", 3),
    MataKuliah("MK007", "Pemograman Berbasis Web", 3),
    MataKuliah("MK008", "Desain Manajemen Jaringan", 5) 
]

daftar_mahasiswa = [
    Mahasiswa("Andi Wijaya", "2912345678", "Teknik Informatika"), 
    Mahasiswa("Budi Santoso", "2311111111", "Sistem Informasi"),
    Mahasiswa("Cindy Lestari", "2322222222", "Teknik Komputer"),
    Mahasiswa("Dedi Pratama", "2333333333", "Sistem Informasi"),
    Mahasiswa("Eva Nurlela", "2344444444", "Teknik Informatika"),
    Mahasiswa("Fani Anggraeni", "2355555555", "Teknik Komputer")
]

kampus = Kampus("Universitas Indonesia", "Bali")

for i, mhs in enumerate(daftar_mahasiswa):
    matkul_diambil = [daftar_matkul[(i + j) % len(daftar_matkul)] for j in range(4 if i % 2 == 0 else 5)]
    for matkul in matkul_diambil:
        mhs.tambah_matkul(matkul)

print("\n" + "=" * 60)
print("DATA MAHASISWA".center(60))
print("=" * 60)
Mahasiswa.jumlah_mahasiswa()
for mhs in daftar_mahasiswa:
    mhs.tampilkan_info()
kampus.tampilkan_info()
