class Tarif:
    def __init__(self, yemek_adi, icindekiler, adimlar):
        self.yemek_adi = yemek_adi
        self.icindekiler = icindekiler
        self.adimlar = adimlar

class TarifUygulamasi:
    def __init__(self):
        self.tarifler = []

    def tarif_ekle(self, yemek_adi, icindekiler, adimlar):
        tarif = Tarif(yemek_adi, icindekiler, adimlar)
        self.tarifler.append(tarif)

    def tarif_goster(self):
        if len(self.tarifler) > 0:
            for i, tarif in enumerate(self.tarifler):
                print(f"\nTarif {i + 1}:")
                print(f"Yemek adı: {tarif.yemek_adi}")
                print("İçindekiler:")
                for i,icindeki in enumerate(tarif.icindekiler):
                    print("{}. {}".format(i+1, icindeki))
                print("Adımlar:")
                for i,adim in enumerate(tarif.adimlar):
                    print("{}. Adım : {}".format(i+1, adim))
        else:
            print("Henüz hiç tarif eklenmemiş.")
    def tarif_guncelle(self, index, yemek_adi, icindekiler, adimlar):
        if len(self.tarifler) > 0:
            self.tarifler[index].yemek_adi = yemek_adi
            self.tarifler[index].icindekiler = icindekiler
            self.tarifler[index].adimlar = adimlar
            print(f"Tarif {index + 1} güncellendi.")
        else:
            print("Geçersiz indeks. Tarif güncellenemedi.")  
    def tarif_sil(self, index):
        if len(self.tarifler) > 0:
            removed_tarif = self.tarifler.pop(index)
            print(f"Tarif '{removed_tarif.yemek_adi}' silindi.")
        else:
            print("Geçersiz indeks. Tarif silinemedi.")      

def main():
    uygulama = TarifUygulamasi()

    while True:
        print("\nTarif Uygulaması Menüsü:")
        print("1. Tarif Ekleme")
        print("2. Tarifleri Gösterme")
        print("3. Tarif Güncelleme")
        print("4. Tarif Silme")
        print("5. Çıkış")

        secim = input("Seçiminizi girin: ")

        if secim == "1":
            yemek_adi = input("Yemek adını girin: ")
            icindekiler = input("İçindekileri girin (virgülle ayrılmış): ").split(',')
            adimlar = input("Adımları girin (her adımı noktalı virgülle ayırarak): ").split(';')
            uygulama.tarif_ekle(yemek_adi, icindekiler, adimlar)
            print("Tarif başarıyla eklendi.")
        elif secim == "2":
            uygulama.tarif_goster()
        elif secim == "3":
            uygulama.tarif_goster()
            index = int(input("Güncellenecek tarifin indeksini girin: ")) - 1
            if 0 <= index < len(uygulama.tarifler):
                yemek_adi = input("Yeni yemek adını girin: ")
                icindekiler = input("Yeni içindekileri girin (virgülle ayrılmış): ").split(',')
                adimlar = input("Yeni adımları girin (her adımı noktalı virgülle ayırarak): ").split(';')
                uygulama.tarif_guncelle(index, yemek_adi, icindekiler, adimlar)
            else:
                print("Geçersiz indeks. Tarif güncellenemedi.")
        elif secim == "4":
            uygulama.tarif_goster()
            index = int(input("Silinecek tarifin indeksini girin: ")) - 1
            uygulama.tarif_sil(index)
        elif secim == "5":
            print("Tarif Uygulaması'ndan çıkılıyor.")
            break
        else:
            print("Geçersiz seçim. Lütfen geçerli bir seçenek seçin.")

if __name__ == "__main__":
    main()