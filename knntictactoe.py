import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

def inicia_algoritmo():
    X = pd.read_csv('./tic-tac-toe-processed.data', sep=',', header=0)
    y = pd.read_csv('./tic-tac-toe-processed.data', sep=',', header=0)
    
    X = X.drop(X.columns[9], axis=1)
    y = y.drop(y.columns[:9], axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.50)

    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    knn = KNeighborsClassifier(n_neighbors=8)
    knn.fit(X_train, np.ravel(y_train))

    y_pred = knn.predict(X_test)

    # print(y_pred)
    # print([1,1,1,1,0,0,1,0,0])

    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

inicia_algoritmo()