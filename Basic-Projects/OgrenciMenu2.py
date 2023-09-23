def menu_goster():
    print("----- Öğrenci Menüsü -----")
    print("1. Öğrenci Ekle")
    print("2. Öğrenci Sil")
    print("3. Öğrenci Bilgilerini Göster")
    print("4. Öğrenci Sınav Sonuçlarına Eriş")
    print("5. Çıkış")
def ogrenci_ekle(ogrenciler):
    ad = input("Eklemek istediğiniz öğrencinin adını giriniz: ")
    soyad = input("Eklemek istediğiniz öğrencinin soyadını giriniz: ")
    numara = input("Eklemek istediğiniz öğrencinin numarasını giriniz: ")
    vize = input("Eklemek istediğiniz öğrencinin vize notunu giriniz: ")
    final = input("Eklemek istediğiniz öğrencinin final notunu giriniz: ")

    ogrenci = {"Ad" : ad, "Soyad" : soyad, "Numara" : numara, "Sınav Sonuçları" : (vize,final)}
    ogrenciler.append(ogrenci)
    print("Öğrenci ekleme işlemi başarılı..")
def ogrenci_Sil(ogrenciler):
    numara = input("Eklemek istediğiniz öğrencinin numarasını giriniz: ")

    for ogrenci in ogrenciler:
        if ogrenci["Numara"] == numara:
            ogrenciler.remove(ogrenci)
            print("Öğrenci silme işlemi başarılı..")
            return
        
    print("Öğrenci bulunamadı..")    
def ogrenci_bilgileri(ogrenciler):
    numara = input("Eklemek istediğiniz öğrencinin numarasını giriniz: ")

    for ogrenci in ogrenciler:
        if ogrenci["Numara"] == numara:
            print("Ad: " + ogrenci["Ad"])
            print("Soyad: " + ogrenci["Soyad"])
            print("Numara: " + ogrenci["Numara"])
            return

    print("Öğrenci bulunamadı..")    
def sinav_sonuclari(ogrenciler):
    numara = input("Eklemek istediğiniz öğrencinin numarasını giriniz: ")

    for ogrenci in ogrenciler:
        if ogrenci["Numara"] == numara:
            print("Sınav Sonuçları:")
            for i,sonuc in enumerate(ogrenci["Sınav Sonuçları"]):
                print("{}. sınav sonucu : {}".format(i+1,sonuc))
            return

    print("Öğrenci bulunamadı..")        
def ana_menu():
    ogrenciler = []
    while True:
        menu_goster()
        secim = input("Yapmak istediğiniz işlemi giriniz: ")

        if secim == "1":
            ogrenci_ekle(ogrenciler)
        elif secim == "2":
            ogrenci_Sil(ogrenciler)
        elif secim == "3":
            ogrenci_bilgileri(ogrenciler)
        elif secim == "4":
            sinav_sonuclari(ogrenciler)
        elif secim == "5":
            print("Çıkış yapılıyor..")
            break
        else:
            print("Geçersiz işlem girdiniz. Lütfen tekrar deneyiniz!")                
if __name__ == "__main__":
    ana_menu()          