from sklearn.datasets import load_iris
from sklearn import tree
from graphviz import Source

iris = load_iris()
X, y = iris.data, iris.target
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

dot_data = tree.export_graphviz(clf, out_file=None)
graph = Source(dot_data)
graph.render("iris")