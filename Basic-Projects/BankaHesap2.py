class BankaHesabı:
    def __init__(self, hesap_sahibi, hesap_no, bakiye = 0):
        self.hesap_sahibi = hesap_sahibi
        self.hesap_no = hesap_no
        self.bakiye = bakiye
    def para_yatir(self, miktar):
        self.bakiye += miktar
        print(f"{self.hesap_sahibi} adlı kullanıcının {self.hesap_no} numaralı hesabına {miktar} TL tutarında para girişi gerçekleşmiştir.")  
    def para_cek(self,miktar):
        if self.bakiye >= miktar:
            self.bakiye -=miktar
            print(f"{self.hesap_sahibi} adlı kullanıcının {self.hesap_no} numaralı hesabından {miktar} TL tutarında para çekme işlemi gerçekleşmiştir.")  
        else:
            print("Yetersiz bakiye..")    
    def bakiye_sorgula(self):
        print(f"{self.hesap_sahibi} adlı kullanıcının {self.hesap_no} numaralı hesabının toplam bakiyesi :  {self.bakiye} TL")        

def menu_goster():
    print("1. Para yatır")
    print("2. Para çek")
    print("3. Bakiye sorgula")
    print("4. Çıkış")
if __name__ == "__main__":
    hesap_sahibi = input("Hesap Sahibinin adını giriniz: ")
    hesap_no = input("Hesap numaranızı giriniz: ")

    hesap = BankaHesabı(hesap_sahibi, hesap_no)

    while True:
        menu_goster()

        secim = input("Yapmak istediğiniz işlemi giriniz: ")

        if secim == "1":
            miktar = float(input("Yatırmak istediğiniz tutarı giriniz: "))
            hesap.para_yatir(miktar)
        elif secim == "2":
            miktar = float(input("Çekmek istediğiniz tutarı giriniz: "))
            hesap.para_cek(miktar)
        elif secim == "3":
            hesap.bakiye_sorgula()
        elif secim == "4":
            print("Çıkış yapılıyor..")
            break
        else:
            print("Hatalı işlem girdiniz. Lütfen tekrar deneyiniz!")
            continue            