import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR
import matplotlib.pyplot as plt

df = pd.read_csv('Salary_Data.csv')

# Memisahkan antara atribut dan label
X = np.array(df['YearsExperience'])
y = df['Salary']

# Mengubah bentuk atribut
#print(X)
X = X[:, np.newaxis]

# Membangun model dengan parameter C, gamma, dan kernel
model = SVR()
parameters = {
    'kernel': ['rbf'],
    'C': [1000, 10000, 100000],
    'gamma': [0.5, 0.05, 0.005]
}
grid_search = GridSearchCV(model, parameters)

# Melatih model dengan fungsi fit()
grid_search.fit(X, y)

# Menampilkan parameter terbaik dari objek grid_search
print(grid_search.best_params_)

# Membuat model SVM baru dengan parameter terbaik hasil grid search
model_baru = SVR(C=100000, gamma=0.05, kernel='rbf')
model_baru.fit(X, y)

plt.scatter(X, y)
plt.plot(X, model_baru.predict(X))
plt.show()