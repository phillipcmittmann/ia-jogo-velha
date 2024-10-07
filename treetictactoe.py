import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def inicia_algoritmo():
    X_train = pd.read_csv('./tic-tac-toe-X-train.data', sep=',', header=0)
    y_train = pd.read_csv('./tic-tac-toe-y-train.data', sep=',', header=0)
    
    tree = DecisionTreeClassifier() # 60 a 70%

    tree.fit(X_train, np.ravel(y_train))

    X_test = pd.read_csv('./tic-tac-toe-X-test.data', sep=',', header=0)
    y_test = pd.read_csv('./tic-tac-toe-y-test.data', sep=',', header=0)

    y_pred = tree.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    return tree

inicia_algoritmo()