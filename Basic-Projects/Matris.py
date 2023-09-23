import numpy as np

def rastgele_matris_olustur(satir, sutun, min_deger=0, max_deger=10):
    return np.random.randint(min_deger, max_deger + 1, size=(satir, sutun))

def matris_toplam(matris):
    return np.sum(matris)

def matris_transpoz(matris):
    return np.transpose(matris)

def matris_carpimi(matris1, matris2):
    return np.dot(matris1, matris2)

if __name__ == "__main__":
    satir_sayisi = int(input("Satır sayısını giriniz: "))
    sutun_sayisi = int(input("Sütun sayısını giriniz: "))

    matris1 = rastgele_matris_olustur(satir_sayisi, sutun_sayisi)

    matris2 = rastgele_matris_olustur(sutun_sayisi, satir_sayisi)

    print("Matris 1:")
    print(matris1)
    print("Matris 2:")
    print(matris2)

    toplam = matris_toplam(matris1)
    print(f"Matris 1'in elemanlarının toplamı: {toplam}")

    toplam2 = matris_toplam(matris2)
    print(f"Matris 2'nin elemanları toplamı: {toplam2}")

    transpoz_matris1 = matris_transpoz(matris1)
    print("Matris 1'in transpozu:")
    print(transpoz_matris1)

    transpoz_matris2 = matris_transpoz(matris2)
    print("Matris 2'in transpozu:")
    print(transpoz_matris2)

    carpim = matris_carpimi(matris1, matris2)
    print("Matrislerin çarpımı:")
    print(carpim)