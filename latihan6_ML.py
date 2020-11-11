import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import linear_model

# Buka File data
df = pd.read_csv('Social_Network_Ads.csv')

# Drop Kolom yang tidak diperlukan
data = df.drop(columns=['User ID'])

# Jalankan proses One hot Encoding
data = pd.get_dummies(data)

# Pisahkan antara atribut dan tabel
predictions = ['Age' , 'EstimatedSalary' , 'Gender_Female' , 'Gender_Male']
X = data[predictions]
y = data['Purchased']

# Melakukan Normalisasi Data
scaler = StandardScaler().fit(X)
scaled_data = scaler.transform(X)
scaled_data = pd.DataFrame(scaled_data, columns=X.columns)
scaled_data.head()

# Bagi data menjadi train dan test untuk setiap atribut dan label
X_train, X_test, y_train, y_test = train_test_split(scaled_data, y, test_size=0.2, random_state=1)

# Latih model dengan fungsi fit
model = linear_model.LogisticRegression().fit(X_train, y_train)

# Uji Akurasi Model
model.score(X_test, y_test)
print(model.score(X_test, y_test))