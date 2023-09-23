import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def en_iyi_filmler(doysa_adi):
    df = pd.read_csv(doysa_adi)

    filmler = df.sort_values(by= 'Rating', ascending= False).head(20)
    print(filmler)

    plt.figure(figsize=(12,8))

    sns.barplot(x= 'Rating', y = 'Name', data= filmler, palette='viridis')

    plt.title("En İyi 20 Film")
    plt.xlabel("IMDB Puanı")
    plt.ylabel("Film Adı")
    
    plt.show()

if __name__ == "__main__":
    dosya = "IMDB.csv"
    en_iyi_filmler(dosya)    
