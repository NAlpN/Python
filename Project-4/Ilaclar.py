import pandas as pd
import matplotlib.pyplot as plt

def ilaclar(dosya):
    df = pd.read_excel(dosya)

    recete_tur = df['ReceteTur'].value_counts()

    plt.figure(figsize=(10,6))

    recete_tur.plot(kind='bar')

    plt.title('Reçete Türü Dağılımı')
    plt.xlabel('Reçete Türü')
    plt.ylabel('Adet')

    plt.show()
if __name__ == "__main__":
    dosya = 'Ilaclar.xlsx'
    ilaclar(dosya)