HesapSahibi = input("Adınızı giriniz: ")
HesapNo = input("Hesap numaranızı giriniz: ")
bakiye = 0
while True:
    print("1. Para yatır")
    print("2. Para çek")
    print("3. Bakiye sorgula")
    print("4. Çıkış")

    secim = input("Yapmak istediğiniz işlemi giriniz: ")

    if secim == "1":
        tutar = float(input("Yatırmak istediğiniz tutarı giriniz: "))
        bakiye += tutar
        print(f"{HesapSahibi} adlı kullanıcının {HesapNo} numaralı hesabına {tutar} TL para yatırma işlemi başarı ile gerçekleşmiştir.")
    elif secim == "2":
        tutar = float(input("Çekmek istediğiniz tutarı giriniz: "))
        if bakiye >= tutar:
            bakiye -= tutar
            print(f"{HesapSahibi} adlı kullanıcının {HesapNo} numaralı hesabından {tutar} TL para çekme işlemi başarı ile gerçekleşmiştir.") 
        else:
            print(f"{HesapSahibi} adlı kullanıcının {HesapNo} numaralı hesabında yeterli bakiye olmadığından işlem gerçekleştirilememiştir.")
    elif secim == "3":
        print(f"{HesapSahibi} adlı kullanıcının {HesapNo} numaralı hesabının toplam bakiyesi: {bakiye}")  
    elif secim == "4":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz bir işlem girdiniz. Lütfen tekrar deneyiniz!")
        continue                 