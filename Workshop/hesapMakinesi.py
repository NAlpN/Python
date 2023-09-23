def topla(sayi1,sayi2):
    return sayi1 + sayi2

def cikar(sayi1,sayi2):
    return sayi1 - sayi2

def carp(sayi1,sayi2):
    return sayi1 * sayi2

def bol(sayi1,sayi2):
    return sayi1 / sayi2

print("Operasyon:")
print("1 : Topla")
print("2 : Çıkar")
print("3 : Çarp")
print("4 : Böl")

secenek = input("Operasyon seçiminiz?")

if secenek == '1':
    sayi1 = int(input("Birinci sayı?"))
    sayi2 = int(input("İkinci sayı?"))
    print("Toplam : " +str(topla(sayi1,sayi2)))
elif secenek == '2':
    sayi1 = int(input("Birinci sayı?"))
    sayi2 = int(input("İkinci sayı?"))
    print("Çıkarma : " +str(cikar(sayi1,sayi2)))   
elif secenek == '3':
    sayi1 = int(input("Birinci sayı?"))
    sayi2 = int(input("İkinci sayı?"))
    print("Çarpma : " +str(carp(sayi1,sayi2))) 
elif secenek == '4':
    sayi1 = int(input("Birinci sayı?"))
    sayi2 = int(input("İkinci sayı?"))
    print("Bölme : " +str(bol(sayi1,sayi2)))