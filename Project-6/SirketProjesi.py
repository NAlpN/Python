import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Top2000CompaniesGlobally.csv')

sirala = df.sort_values(by=["Profits ($billion)"], ascending= False)
print(sirala[["Company", "Profits ($billion)"]].head(10))

sns.barplot(x='Company', y='Profits ($billion)', data=sirala.head(10))
plt.xticks(rotation=90)
plt.title("En Karlı 10 Şirket")
plt.tight_layout()
plt.show()