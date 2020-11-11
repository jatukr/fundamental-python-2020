import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

df = pd.read_csv('diabetes.csv')
#print(df.info())

# Memisahkan atribut pada dataset dan menyimpannya pada sebuah variabek
X = df[df.columns[:8]]
#print(X)

# memisahkan label pada dataset dan menyimpannya pada sebuah variabel
y = df['Outcome']

# standarisasi nilai-nilai dari dataset
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

# Memisahkan data untuk training dan testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=43)

# Membuat objek svc dan memanggil fungsi fit untuk melatih model
clf = SVC()
clf.fit(X_train, y_train)

# Menampilkan skor akurasi prediksi
print(clf.score(X_test, y_test))
