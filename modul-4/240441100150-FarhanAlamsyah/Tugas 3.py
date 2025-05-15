class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan

    @property
    def info(self):
        return f"{self.__nama}, {self.__umur} tahun, Keluhan: {self.__keluhan}"


class Klinik:
    def __init__(self):
        self.daftar_pasien = []

    def tambah_pasien(self):
        nama = input("\nMasukkan Nama Pasien: ")
        umur_input = input("Masukkan Umur: ")
        if not umur_input.isdigit():
            print("\nUmur harus berupa angka.")
            return
        umur = int(umur_input)
        keluhan = input("Masukkan Keluhan: ")
        self.daftar_pasien.append(Pasien(nama, umur, keluhan))
        print("\nData pasien berhasil ditambahkan!".center(50))

    def tampilkan_pasien(self):
        if not self.daftar_pasien:
            print("\nBelum ada pasien yang terdaftar.")
            return
        print("\nDaftar Pasien".center(50))
        print("-" * 50)
        for pasien in self.daftar_pasien:
            print(pasien.info)
        print("-" * 50)


if __name__ == "__main__":
    klinik = Klinik()
    while True:
        print()
        print("-" * 50)
        print("MENU KLINIK".center(50))
        print("-" * 50)
        print("Pilih Menu:")
        print("1. Tambah Pasien")
        print("2. Tampilkan Daftar Pasien")
        print("0. Keluar")
        print("-" * 50)
        pilihan = input("Pilih: ")
        print("-" * 50)

        if pilihan == '1':
            klinik.tambah_pasien()
        elif pilihan == '2':
            klinik.tampilkan_pasien()
        elif pilihan == '0':
            print("\nProgram selesai. Terima kasih!")
            break
        else:
            print("\nPilihan tidak valid.")




