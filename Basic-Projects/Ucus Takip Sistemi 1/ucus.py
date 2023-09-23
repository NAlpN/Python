class Ucus:
    def __init__(self, ucus_no, kalkis_yeri,varis_yeri,kalkis_tarihi,varis_tarihi):
        self.ucus_no = ucus_no
        self.kalkis_yeri = kalkis_yeri
        self.varis_yeri = varis_yeri
        self.kalkis_tarihi = kalkis_tarihi
        self.varis_tarihi = varis_tarihi
        self.yolcular = []
    def yolcu_ekle(self, yolcu):
        self.yolcular.append(yolcu) 
    def yolcu_sil(self, yolcu):
        self.yolcular.remove(yolcu)
    def bilgiler(self):
        print("Uçuş Numarası: ", self.ucus_no)
        print("Kalkış Yeri: ", self.kalkis_yeri)
        print("Varış Yeri: ", self.varis_yeri)
        print("Kalkış Tarihi: ", self.kalkis_tarihi)
        print("Varış Yeri: ", self.varis_tarihi) 
        print("Yolcular:")
        for yolcu in self.yolcular:
            print(yolcu.ad, yolcu.soyad, "Koltuk: ", yolcu.koltuk_no)