from ucus import Ucus
from yolcu import Yolcu

ucus_listesi = []
yolcu_listesi = []

def yeni_ucus():
    ucus_no = input("Eklemek istediğiniz uçuşun numarasını giriniz: ")
    kalkis_yeri = input("Eklemek istediğiniz uçuşun kalkış yerini giriniz: ")
    varis_yeri = input("Eklemek istediğiniz uçuşun varış yerini giriniz: ")
    kalkis_tarihi = input("Eklemek istediğiniz uçuşun kalkış tarihini giriniz: ")
    varis_tarihi = input("Eklemek istediğiniz uçuşun varış tarihini giriniz: ")

    ucus = Ucus(ucus_no, kalkis_yeri, varis_yeri, kalkis_tarihi, varis_tarihi)
    ucus_listesi.append(ucus)
def yolcu_ekle():
    ad = input("Eklemek istediğiniz yolcunun adını giriniz: ")
    soyad = input("Eklemek istediğiniz yolcunun soyadını giriniz: ")
    koltuk_no = input("Eklemek istediğiniz yolcunun koltuk numarasını giriniz: ")

    yolcu = Yolcu(ad, soyad, koltuk_no)

    print("Uçuş Listesi:")
    for index, ucus in enumerate(ucus_listesi):
        print(index+1, "-", ucus.ucus_no, "Kalkış Yeri: ", ucus.kalkis_yeri, "Varış Yeri: ", ucus.varis_yeri)

    ucus_index = int(input("Kaç numaralı uçuşa yolcu eklemek istersiniz: "))
    ucus = ucus_listesi[ucus_index - 1]
    ucus.yolcu_ekle(yolcu)
def yolcu_sil():
    print("Uçuş Listesi:")
    for index, ucus in enumerate(ucus_listesi):
        print(index+1, "-", ucus.ucus_no, "Kalkış Yeri: ", ucus.kalkis_yeri, "Varış Yeri: ", ucus.varis_yeri)
    ucus_index = int(input("Kaç numaralı uçuştan yolcu silmek istersiniz: "))  
    ucus = ucus_listesi[ucus_index - 1]

    print("Yolcu Listesi:")
    for index, yolcu in enumerate(ucus.yolcular):
        print(index+1, "-", ucus.ucus_no, "Kalkış Yeri: ", ucus.kalkis_yeri, "Varış Yeri: ", ucus.varis_yeri)

    yolcu_index = int(input("Kaç numaralı yolcuyu silmek istersiniz: "))
    yolcu = ucus.yolcular[yolcu_index - 1]     

    ucus.yolcu_sil(yolcu)   
def bilgiler():
    print("Uçuş Listesi:")
    for index,ucus in enumerate(ucus_listesi):
        print(index+1, "-", ucus.ucus_no, "Kalkış Yeri: ", ucus.kalkis_yeri, "Varış Yeri: ", ucus.varis_yeri)

    ucus_index = int(input("Kaç numaralı uçuşun bilgilerini görüntülemek istersiniz: "))
    ucus = ucus_listesi[ucus_index -1]
    ucus.bilgiler()
def menu_goster():
        print("Menü:")
        print("1. Yeni Uçuş Oluştur")
        print("2. Yolcu Ekle")
        print("3. Yolcu Sil")
        print("4. Uçuş Bilgilerini Görüntüle")
        print("5. Çıkış")
if __name__ == "__main__":
    while True:
        menu_goster()
        secim = input("Yapmak istediğiniz işlemi seçiniz: ")

        if secim == "1":
            yeni_ucus()
        elif secim == "2":
            yolcu_ekle()
        elif secim == "3":
            yolcu_sil()
        elif secim == "4":
            bilgiler()
        elif secim == "5":
            print("Çıkış yapılıyor.")
            break
        else:
            print("Tekrar deneyiniz!")
            continue                 
      
