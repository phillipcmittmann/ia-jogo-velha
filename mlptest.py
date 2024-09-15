from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Generate a random n-class classification problem.
X, y = make_classification(n_samples=100, random_state=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y,
                                                    random_state=1)

# Fit the model to data matrix X and target(s) y.
clf = MLPClassifier(random_state=1, max_iter=300).fit(X_train, y_train)

print(clf.predict_proba(X_test[:1]))