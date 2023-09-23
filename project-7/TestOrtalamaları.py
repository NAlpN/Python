import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_marks.csv")


test_ortalama = df.mean()

test_no = df.columns[1:]
 
plt.figure(figsize=(10, 6))
plt.plot(test_no, test_ortalama[1:], marker='o', label = 'Test Ortalamaları')
plt.title('Testlerin Not Ortalamaları Analizi')
plt.xlabel('Test')
plt.ylabel('Ortalama')
plt.xticks(rotation=45)
plt.grid(True)

plt.legend()
plt.show()