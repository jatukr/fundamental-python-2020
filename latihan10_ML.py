import pandas as pd
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

df = pd.read_csv('Salary_Data.csv')
print(df.info())

# Memisahkan antara atribut dan label
X = np.array(df['YearsExperience'])
y = df['Salary']

# Mengubah bentuk atribut
#print(X)
X = X[:, np.newaxis]
#print(X)

# Membangun model dengan parameter C, gamma, dan kernel
model = SVR(C=1000, gamma=0.05, kernel='rbf')

# Melatih model dengan fungsi fit()
model.fit(X, y)

# Memvisualisasikan model
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.show()

