import sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
x = iris.data
y = iris.target

print(x)
print(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print(len(x_test))
