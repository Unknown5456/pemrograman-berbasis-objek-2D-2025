class RekeningBank:
    def __init__(self, no_rek, nama_pemilik, saldo=0):
        self.__no_rek = no_rek
        self.__nama_pemilik = nama_pemilik
        self.__saldo = saldo

    @property
    def no_rek(self):
        return self.__no_rek

    @property
    def nama_pemilik(self):
        return self.__nama_pemilik

    @property
    def saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("\nSaldo tidak cukup atau jumlah tidak valid.")

    def info(self):
        return f"{self.__no_rek} | {self.__nama_pemilik} | Saldo: {self.__saldo}"


class Bank:
    def __init__(self):
        self.rekening_list = []

    def tambah_rekening(self):
        no_rek = input("\nMasukkan Nomor Rekening: ")
        if not no_rek.isdigit():
            print("\nNomor rekening harus berupa angka.")
            return

        if self.cari_rekening(no_rek):
            print("\nNomor rekening sudah terdaftar.")
            return

        nama = input("Masukkan Nama Pemilik: ")
        saldo_input = input("Masukkan Saldo Awal: ")
        if not saldo_input.isdigit():
            print("\nSaldo harus berupa angka.")
            return

        saldo = int(saldo_input)
        self.rekening_list.append(RekeningBank(no_rek, nama, saldo))
        print("\nRekening berhasil ditambahkan".center(40))

    def cari_rekening(self, no_rek):
        for rek in self.rekening_list:
            if rek.no_rek == no_rek:
                return rek
        return None

    def setor_atau_tarik(self):
        no = input("Masukkan Nomor Rekening: ")
        rek = self.cari_rekening(no)
        if rek:
            opsi = input("Setor / Tarik : ").lower()
            jumlah_input = input("Masukkan jumlah: ")
            if not jumlah_input.isdigit():
                print("\nJumlah harus berupa angka.")
                return
            jumlah = int(jumlah_input)

            if opsi == 'setor':
                rek.setor(jumlah)
                print(f"\n[Setor] sebesar Rp {jumlah} berhasil. Saldo sekarang: {rek.saldo}")
            elif opsi == 'tarik':
                rek.tarik(jumlah)
                print(f"\n[Tarik] sebesar Rp {jumlah} berhasil. Saldo sekarang: {rek.saldo}")
            else:
                print("\nOpsi tidak valid.")
        else:
            print("\nRekening tidak ditemukan.")

    def tampilkan_semua(self):
        if not self.rekening_list:
            print("\nTidak ada rekening yang terdaftar.")
            return
        print()
        print("Daftar Rekening".center(50))
        for rek in self.rekening_list:
            print(rek.info())
        print("-" * 50)


if __name__ == "__main__":
    bank = Bank()
    while True:
        print()
        print("-" * 50)
        print("MENU BANK".center(50))
        print("-" * 50)
        print("Pilih Menu:")
        print("1. Tambah Rekening")
        print("2. Setor / Tarik")
        print("3. Tampilkan Semua Rekening")
        print("0. Keluar")
        print("-" * 50)
        pilihan = input("Pilih: ")
        print("-" * 50)

        if pilihan == '1':
            bank.tambah_rekening()
        elif pilihan == '2':
            bank.setor_atau_tarik()
        elif pilihan == '3':
            bank.tampilkan_semua()
        elif pilihan == '0':
            print("\nProgram selesai. Terima kasih!")
            break
        else:
            print("\nPilihan tidak valid.")
