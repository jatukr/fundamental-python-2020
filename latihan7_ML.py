import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Mall_Customers.csv')
#print(df.head(3))

# Rename kolom
df = df.rename(columns={'Gender': 'gender', 'Age': 'age',
                        'Annual Income (k$)': 'annual_income',
                        'Spending Score (1-100)': 'spending_score'})

# Ubah data kategorik menjadi numerik
df['gender'].replace(['Female', 'Male'], [0, 1], inplace=True)
#print(df)

# Menghilangkan kolom kustomer
#help(df.drop)
X = df.drop(['CustomerID', 'gender'], axis=1)

# Membuat list yang berisi inertia
cluster = []
for i in range(1,11):
    km = KMeans(n_clusters=i).fit(X)
    cluster.append(km.inertia_)

# Membuat plot inertia
fig, ax = plt.subplots(figsize=(8, 4))
sns.lineplot(x=list(range(1, 11)), y=cluster, ax=ax)
ax.set_title('Cari Elbow')
ax.set_label('Clusters')
ax.set_ylabel('Inertia')
#plt.show(), Menunjukkan hasil K/Cluster optimal di 5

# Membuat Objek K-Means
km5 = KMeans(n_clusters=5).fit(X)

# Menambahkan kolom label pada dataset
X['labels'] = km5.labels_
print(X)

# Membuat plot KMeans dengan 5 Klaster
plt.figure(figsize=(8,4))
sns.scatterplot(X['annual_income'], X['spending_score'], hue=X['labels'],
                palette=sns.color_palette('hls', 5))
plt.title('KMeans dengan 5 cluster')
plt.show()