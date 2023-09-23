def ucus_takip():
    while True:
        print("Uçuş Takip Sistemi")
        print("------------------")
        print("1. Uçuşları Listele")
        print("2. Uçuş Ekle")
        print("3. Uçuş Sil")
        print("4. Çıkış")
        
        secim = input("Bir seçenek seçin: ")
        
        if secim == "1":
            ucuslari_listele()
        elif secim == "2":
            ucus_ekle()
        elif secim == "3":
            ucus_sil()    
        elif secim == "4":
            print("Uçuş takip sisteminden çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek! Tekrar deneyin.")
        
        print("------------------")
        
def ucuslari_listele():
    # Uçuşları listeleme işlemi burada gerçekleştirilir
    with open('ucuslar.txt', 'r') as dosya:
        ucuslar = dosya.readlines()
    
    for ucus in ucuslar:
        ucus_bilgileri = ucus.split(',')
        ucus_no = ucus_bilgileri[0]
        kalkis = ucus_bilgileri[1]
        varis = ucus_bilgileri[2]
        kalkis_zamani = ucus_bilgileri[3]
        varis_zamani = ucus_bilgileri[4].strip()
        
        print(f"Uçuş No: {ucus_no}")
        print(f"Nokta: {kalkis}")
        print(f"Hedef: {varis}")
        print(f"Kalkış Zamanı: {kalkis_zamani}")
        print(f"Varış Zamanı: {varis_zamani}")
        print("-----")

def ucus_ekle():
    # Yeni uçuş ekleme işlemi burada gerçekleştirilir
    ucus_no = input("Uçuş No: ")
    kalkis = input("Kalkış Yeri: ")
    varis = input("Varış Yeri: ")
    kalkis_zamani = input("Kalkış Zamanı: ")
    varis_zamani = input("Varış Zamanı: ")
    
    ucus_bilgisi = f"{ucus_no},{kalkis},{varis},{kalkis_zamani},{varis_zamani}\n"
    
    with open('ucuslar.txt', 'a') as dosya:
        dosya.write(ucus_bilgisi)
    
    print("Uçuş başarıyla eklendi.")

def ucus_sil():
    ucus_no = input("İptal etmek istediğiniz uçuşun numarasını giriniz: ")

    with open('ucuslar.txt', 'r') as dosya:
        ucuslar = dosya.readlines()

    with open('ucuslar.txt', 'w') as dosya:
        for ucus in ucuslar:
            ucus_bilgileri = ucus.split(',')
            if ucus_bilgileri[0] != ucus_no:
                dosya.write(ucus)

    print("Uçuş başarıyla silindi.")

ucus_takip()
