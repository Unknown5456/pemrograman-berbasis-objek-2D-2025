class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan

    def estimasi_waktu(self):
        waktu = 5   

class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        super().__init__(asal, tujuan,)
        self.jenis_kendaraan = jenis_kendaraan

    def estimasi_waktu(self):
        if self.jenis_kendaraan.lower() == "truk":
            waktu = 2
        else:
            waktu = 1
        return (waktu + super().estimasi_waktu())
    
class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai.lower() == "garuda":
            waktu = 3
        else:
            waktu = 4
        return (waktu + super().estimasi_waktu())

class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        PengirimanDarat.__init__(self, asal, tujuan, jenis_kendaraan)
        PengirimanUdara.__init__(self, asal, tujuan, maskapai)
        self.maskapai = maskapai
        self.jenis_kendaraan = jenis_kendaraan

    def estimasi_waktu(self):
        waktu = 3
        return (waktu + super().estimasi_waktu())


pengiriman_list = []
jumlah = int(input("Masukkan jumlah pengiriman: "))

for i in range(jumlah):
    print(f"\n--- Data Pengiriman ke-{i+1} ---")
    
    internasional = input("Apakah pengiriman internasional? (ya/tidak): ").strip().lower() == "ya"
    
    if internasional:
        while True:
            maskapai = input("Pilih maskapai (Garuda/Lion): ").strip().lower()
            if maskapai in ["garuda", "lion"]:
                break
            else:
                print("❌ Maskapai tidak valid. Pilih antara Garuda atau Lion.")
        asal = input("Masukkan kota asal             : ")
        tujuan = input("Masukkan negara tujuan         : ")
        pengiriman = PengirimanUdara(asal, tujuan, maskapai)
        kendaraan = "-"
    else:
        jenis_kendaraan = input("Jenis Kendaraan (Truk/Motor)   : ")
        asal = input("Masukkan kota asal             : ")
        tujuan = input("Masukkan kota tujuan           : ")
        pengiriman = PengirimanDarat(asal, tujuan, jenis_kendaraan)
        maskapai = "-"

    pengiriman_list.append({
        "objek": pengiriman,
        "asal": asal,
        "tujuan": tujuan,
        "maskapai": maskapai if internasional else "-",
        "kendaraan": "-" if internasional else jenis_kendaraan,
        "internasional": "Ya" if internasional else "Tidak"
    })

# Output
print("\n" + "="*60)
print("📦 ESTIMASI PENGIRIMAN 📦")
print("="*60)

for i, data in enumerate(pengiriman_list, 1):
    print(f"📦 Pengiriman ke-{i}")
    print(f"🌍 Dari           : {data['asal']}")
    print(f"📍 Tujuan         : {data['tujuan']}")
    print(f"🌐 Internasional  : {data['internasional']}")
    print(f"✈️ Maskapai        : {data['maskapai']}")
    print(f"🚚 Kendaraan       : {data['kendaraan']}")
    print(f"⏳ Estimasi Waktu  : {data['objek'].estimasi_waktu()} hari")
    print("-"*60)
