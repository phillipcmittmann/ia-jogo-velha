import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def inicia_algoritmo():
    X = pd.read_csv('./tic-tac-toe-processed.data', sep=',', header=0)
    y = pd.read_csv('./tic-tac-toe-processed.data', sep=',', header=0)
    
    X = X.drop(X.columns[9], axis=1)
    y = y.drop(y.columns[:9], axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.70)

    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    mlp = MLPClassifier(hidden_layer_sizes=(32, 16), max_iter=1000, random_state=42)
    mlp.fit(X_train, np.ravel(y_train))

    # y_pred = mlp.predict(X_test)

    # accuracy = accuracy_score(y_test, y_pred)
    # print("Accuracy:", accuracy)

    # class_report = classification_report(y_test, y_pred)
    # print("Classification Report:\n", class_report)

    return mlp

inicia_algoritmo()
