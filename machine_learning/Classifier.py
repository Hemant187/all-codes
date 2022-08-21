from cProfile import label
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
# print(iris.keys())
print(iris.DESCR)
features = iris.data
labels = iris.target
# print(features[0],labels[0]) 
  # Iris-Setosa
  # - Iris-Versicolour
  # - Iris-Virginica

# Training the classifier
clf = KNeighborsClassifier()
clf.fit(features, labels)

preds = clf.predict([[9.1, 9.5, 6.2, 1]])
print(preds)