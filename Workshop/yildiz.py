def ucgen_olustur(yildiz_sayisi):
    for i in range(1, yildiz_sayisi + 1):
        print('*' * i)

yildiz_sayisi = int(input("Üçgenin yıldız sayısını girin: "))
ucgen_olustur(yildiz_sayisi)
