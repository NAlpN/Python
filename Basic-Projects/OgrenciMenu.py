ogrenciler = []

while True:
    print("----- Öğrenci Menüsü -----")
    print("1. Öğrenci Ekle")
    print("2. Öğrenci Sil")
    print("3. Öğrenci Bilgilerini Göster")
    print("4. Öğrenci Sınav Sonuçlarına Eriş")
    print("5. Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçiniz: ")

    if secim == "1":
        ad = input("Eklemek istediğiniz öğrencinin adını giriniz: ")
        soyad = input("Eklemek istediğiniz öğrencinin soyadını giriniz: ")
        numara = input("Eklemek istediğiniz öğrencinin numarasını giriniz: ")
        sinav1 = input("Eklemek istediğiniz öğrencinin 1. sınav sonucunu giriniz: ") 
        sinav2 = input("Eklemek istediğiniz öğrencinin 2. sınav sonucunu giriniz: ")

        ogrenci = {"Ad" : ad, "Soyad" : soyad, "Numara" : numara, "Sınav Sonuçları" : (sinav1,sinav2)}
        ogrenciler.append(ogrenci)
    elif secim == "2":
        numara = input("Eklemek istediğiniz öğrencinin numarasını giriniz: ")

        for ogrenci in ogrenciler:
            if ogrenci["Numara"] == numara:
                ogrenciler.remove(ogrenci)
                print("Öğrenci silme işlemi başarılı.")
                break
        else:
            print("Girdiğiniz numaraya ait kayıtlı bir öğrenci bulunamadı.")
    elif secim == "3":
        numara = input("Eklemek istediğiniz öğrencinin numarasını giriniz: ")

        for ogrenci in ogrenciler:
            if ogrenci["Numara"] == numara:
                print("Ad: " + ogrenci["Ad"])
                print("Soyad:" + ogrenci["Soyad"])
                print("Numara" + ogrenci["Numara"])
                break
        else:
            print("Girdiğiniz numaraya ait kayıtlı bir öğrenci bulunamadı.")
    elif secim == "4":
        numara = input("Eklemek istediğiniz öğrencinin numarasını giriniz: ")

        for ogrenci in ogrenciler:
            if ogrenci["Numara"] == numara:
                for i,sonuc in enumerate(ogrenci["Sınav Sonuçları"]):
                    print("{}. sınav sonucu: {}".format(i+1,sonuc))
                break
        else:
            print("Girdiğiniz numaraya ait kayıtlı bir öğrenci bulunamadı.")
    elif secim == "5":
        print("Çıkış yapılıyor.")
        break
    else:
        print("Geçersiz bir işlem girdiniz. Lütfen tekrar deneyiniz!")
        continue