class Buku:
    def __init__(self, judul, penulis, halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__halaman = halaman

    @property
    def info(self):
        return f"{self.__judul} oleh {self.__penulis}, {self.__halaman} halaman"


class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self):
        judul = input("\nMasukkan Judul Buku: ")
        penulis = input("Masukkan Nama Penulis: ")
        halaman_input = input("Masukkan Jumlah Halaman: ")
        if not halaman_input.isdigit():
            print("\nJumlah halaman harus berupa angka.")
            return
        halaman = int(halaman_input)
        self.daftar_buku.append(Buku(judul, penulis, halaman))
        print("\nBuku berhasil ditambahkan!".center(50))

    def tampilkan_buku(self):
        if not self.daftar_buku:
            print("\nBelum ada buku yang ditambahkan.")
            return
        print("\nDaftar Buku".center(50))
        print("-" * 50)
        for buku in self.daftar_buku:
            print(buku.info)
        print("-" * 50)


if __name__ == "__main__":
    perpustakaan = Perpustakaan()
    while True:
        print()
        print("-" * 50)
        print("MENU PERPUSTAKAAN".center(50))
        print("-" * 50)
        print("Pilih Menu:")
        print("1. Tambah Buku")
        print("2. Tampilkan Daftar Buku")
        print("0. Keluar")
        print("-" * 50)
        pilihan = input("Pilih: ")
        print("-" * 50)

        if pilihan == '1':
            perpustakaan.tambah_buku()
        elif pilihan == '2':
            perpustakaan.tampilkan_buku()
        elif pilihan == '0':
            print("\nProgram selesai. Terima kasih!")
            break
        else:
            print("\nPilihan tidak valid.")
