# İlk matrisin boyutlarını kullanıcıdan alın
m = int(input("İlk matrisin satır sayısını girin: "))
n = int(input("İlk matrisin sütun sayısını girin: "))

# İkinci matrisin boyutlarını kullanıcıdan alın
p = int(input("İkinci matrisin satır sayısını girin: "))
q = int(input("İkinci matrisin sütun sayısını girin: "))

# Matrislerin boyutları uyumlu mu kontrol edilir
if m != p or n != q:
    print("Matrislerin boyutları uyumsuz. Toplama işlemi yapılamaz.")
else:
    # İlk matrisin elemanlarını kullanıcıdan alın
    print("İlk matrisin elemanlarını girin:")
    matris1 = []
    for i in range(m):
        satir = []
        for j in range(n):
            eleman = int(input("Matris[{}][{}] = ".format(i, j)))
            satir.append(eleman)
        matris1.append(satir)

    # İkinci matrisin elemanlarını kullanıcıdan alın
    print("İkinci matrisin elemanlarını girin:")
    matris2 = []
    for i in range(p):
        satir = []
        for j in range(q):
            eleman = int(input("Matris[{}][{}] = ".format(i, j)))
            satir.append(eleman)
        matris2.append(satir)

    # Matrisleri topla
    sonuc = []
    for i in range(m):
        satir = []
        for j in range(n):
            eleman = matris1[i][j] + matris2[i][j]
            satir.append(eleman)
        sonuc.append(satir)

    # Sonucu ekrana yazdır
    print("Matrislerin toplamı:")
    for satir in sonuc:
        print(satir)
