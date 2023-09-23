import pandas as pd

class kitaplık():
    def __init__(self):
        self.kitap = pd.DataFrame(columns=['Kitap Adı', 'Kitap Yazarı', 'Cilt'])

    def ekle(self, kitap_adi, kitap_yazari, cilt):
        yeni_kitap = pd.DataFrame([[kitap_adi, kitap_yazari, cilt]], columns=['Kitap Adı', 'Kitap Yazarı', 'Cilt'])
        self.kitap = pd.concat([self.kitap, yeni_kitap], ignore_index=True)
        print(f"{kitap_adi} adlı kitap kataloga eklendi.")

    def sil(self, kitap_adi):
        self.kitap = self.kitap[self.kitap['Kitap Adı'] != kitap_adi]
        print(f"{kitap_adi} adlı kitap katalogdan silindi.")

    def goruntule(self):
        print("Kitaplar")
        print(self.kitap)

if __name__ == "__main__":
    kitaplik = kitaplık()

    while True:
        print("\n1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitapları Görüntüle")
        print("4. Çıkış")
        secim = input("Seçiminizi yapın (1/2/3/4): ")

        if secim == "1":
            kitap_adi = input("Kitabın adı: ")
            kitap_yazari = input("Kitabın yazarı: ")
            cilt = input("Kitabın kaçıncı cildi: ")
            kitaplik.ekle(kitap_adi, kitap_yazari, cilt)
        elif secim == "2":
            kitap_adi = input("Silmek istediğiniz kitabın adı: ")
            kitaplik.sil(kitap_adi)
        elif secim == "3":
            kitaplik.goruntule()
        elif secim == "4":
            print("Katalogdan çıkış yapılıyor..")
            break
        else:
            print("Hatalı bir işlem yaptınız! Lütfen tekrar deneyiniz..")
            continue
