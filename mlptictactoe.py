import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report

def inicia_algoritmo():
    X_train = pd.read_csv('./tic-tac-toe-X-train.data', sep=',', header=0)
    y_train = pd.read_csv('./tic-tac-toe-y-train.data', sep=',', header=0)
    
    mlp = MLPClassifier(hidden_layer_sizes=(32, 16), max_iter=1000, random_state=42) # 75 a 90%
    mlp.fit(X_train, np.ravel(y_train))

    X_test = pd.read_csv('./tic-tac-toe-X-test.data', sep=',', header=0)
    y_test = pd.read_csv('./tic-tac-toe-y-test.data', sep=',', header=0)

    y_pred = mlp.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    class_report = classification_report(y_test, y_pred)
    print("Classification Report:\n", class_report)

    return mlp

inicia_algoritmo()
