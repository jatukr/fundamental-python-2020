import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz

# Membaca data csv
iris = pd.read_csv('iris_species/Iris.csv')
# print(iris.head())

# Menghapus Kolom ID
iris.drop('Id', axis=1, inplace=True)
# print(iris.head())

# Memisahkan atribut dan label
X = iris[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = iris['Species']

# Membuat model Decision Tree
tree_model = DecisionTreeClassifier()
tree_model.fit(X, y)

# Prediksi model dengan tree_model.predict([[SepalLength, SepalWidth, PetalLength, PetalWidth]])
print(tree_model.predict([[6.2, 3.4, 5.4, 2.3]]))

export_graphviz(
    tree_model,
    out_file="iris_tree.dot",
    feature_names=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'],
    class_names=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'],
    rounded=True,
    filled=True,
)
