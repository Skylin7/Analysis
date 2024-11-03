import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")  # Grafikler için daha iyi bir görünüm
# Veriyi yükle
data = pd.read_csv('reviews.csv')

# İlk birkaç satırı inceleyerek veri hakkında bilgi alın
print(data.head())
print(data.info())
# Puanların ortalamasını hesapla
score_mean = data['score'].mean()
print(f'Ortalama Puan: {score_mean}')

# Puan dağılımını görselleştir
plt.figure(figsize=(8, 5))
sns.countplot(x='score', data=data, palette='viridis')
plt.title(f'Puan Dağilimi (Ortalama Puan: {score_mean:.2f})')
plt.xlabel('Puan')
plt.ylabel('Yorum Sayisi')
plt.show()

# Tarih sütununu datetime formatına çevir
data['at'] = pd.to_datetime(data['at'])

# Aylık yorum sayısını hesapla
monthly_reviews = data.set_index('at').resample('M').size()

# Aylık ortalama puanları hesapla
monthly_avg_score = data.set_index('at').resample('M')['score'].mean()

# Aylık yorum sayısını çiz
plt.figure(figsize=(10, 5))
monthly_reviews.plot(color='blue')
plt.title('Aylik Yorum Sayisi')
plt.xlabel('Tarih')
plt.ylabel('Yorum Sayisi')
plt.show()

# Aylık ortalama puanı çiz
plt.figure(figsize=(10, 5))
monthly_avg_score.plot(color='orange')
plt.title('Aylik Ortalama Puan')
plt.xlabel('Tarih')
plt.ylabel('Ortalama Puan')
plt.show()
low_score_reviews = data[data['score'] <= 2]
print(f"Kötü yorum sayisi: {len(low_score_reviews)}")

plt.figure(figsize=(6, 4))
low_score_reviews['score'].value_counts().sort_index().plot(kind='bar', color='red')
plt.title("Kötü Yorumlarin Puan Dağilimi")
plt.xlabel("Puan")
plt.ylabel("Yorum Sayisi")
plt.show()
