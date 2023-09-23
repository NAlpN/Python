import random

def oyun():
    data = ["Taş", "Kağıt", "Makas"]

    oyuncu_puan = 0
    rakip_puan = 0
    while True:
        secim = input("Taş Kağıt ya da Makas? (Çıkış için e tuşuna basınız.)").capitalize()

        if secim == 'E':
            print("Oyundan çıkılıyor.")
            break
        if secim not in data:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyiniz.")
            continue
        
        rakip = random.choice(data)
        print(f"Rakip: {rakip}")

        if secim == rakip:
            print("Berabere!")
        elif (secim == "Taş" and rakip == "Makas") or (secim == "Kağıt" and rakip == "Taş") or (secim == "Makas" and rakip == "Kağıt"):
            oyuncu_puan += 1
            print(f"Tebrikler! kazandınız. Oyuncu: {oyuncu_puan}, Rakip: {rakip_puan}")
        else:
            rakip_puan += 1  
            print(f"Rakip Kazandı! Oyuncu: {oyuncu_puan}, Rakip: {rakip_puan}") 

        if oyuncu_puan == 3 or rakip_puan == 3:
            print("Oyun Bitti!")
            if oyuncu_puan == 3:
                print("Tebrikler! Oyuncu Kazandı.")
            else:
                print("Rakip kazandı!")
            break            
if __name__ == "__main__":
    oyun()             