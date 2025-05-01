# Class dasar
class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama       : {self.nama}")
        print(f"Gaji       : {self.gaji}")
        print(f"Departemen : {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        super().info()
        print(f"Tunjangan  : {self.tunjangan}")
        print(f"Status     : Karyawan Tetap")
        print("-" * 30)

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        super().info()
        print(f"Jam Kerja  : {self.jam_kerja} jam/hari")
        print(f"Status     : Karyawan Harian")
        print("-" * 30)

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        print("\nDaftar Seluruh Karyawan:\n" + "=" * 30)
        for karyawan in self.daftar_karyawan:
            karyawan.info()

manajemen = ManajemenKaryawan()

jumlah = int(input("Berapa jumlah karyawan yang ingin ditambahkan? "))

for i in range(jumlah):
    print(f"\n--- Data Karyawan ke-{i+1} ---")
    nama = input("Nama: ")
    gaji = int(input("Gaji: "))
    departemen = input("Departemen: ")
    status = input("Status (Tetap/Harian): ").strip().lower()

    if status == "tetap":
        tunjangan = int(input("Tunjangan: "))
        karyawan = KaryawanTetap(nama, gaji, departemen, tunjangan)
    elif status == "harian":
        jam_kerja = int(input("Jam Kerja per hari: "))
        karyawan = KaryawanHarian(nama, gaji, departemen, jam_kerja)
    else:
        print("Status tidak valid. Lewati entri ini.")
        continue

    manajemen.tambah_karyawan(karyawan)

manajemen.tampilkan_semua_karyawan()
