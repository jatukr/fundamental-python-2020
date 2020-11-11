import sklearn
from sklearn import tree, datasets
from sklearn.model_selection import cross_val_score

# Load data iris
iris = datasets.load_iris()

x = iris.data
y = iris.target

# membuat model dengan tree
clf = tree.DecisionTreeClassifier()

# Mengevaluasi performa model dengan cross_val_score
scores = cross_val_score(clf, x, y, cv=5)
print(scores)
