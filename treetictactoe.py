from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

data = pd.read_csv('./tic-tac-toe-processed.data', sep=',', header=0)

X = data
y = data['result']

# aumentar tamanho do teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

tree = DecisionTreeClassifier()

tree.fit(X_train, y_train)

y_pred = tree.predict(X_test)