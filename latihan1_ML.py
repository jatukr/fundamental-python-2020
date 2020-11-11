import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler

df_data_1 = pd.read_csv('iris_species/Iris.csv')
print(df_data_1.head())

data = [[12000000, 33], [35000000, 45], [4000000, 23], [6500000, 26], [9000000, 29]]

# scaler = MinMaxScaler()
# print(scaler.fit(data))
# print(scaler.transform(data))
scaler = preprocessing.StandardScaler().fit(data)
print(scaler)
data = scaler.transform(data)
print(data)