import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

def inicia_algoritmo():
    data = pd.read_csv('./tic-tac-toe-processed.data', sep=',', header=0)

    X = data
    y = data['result']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    knn = KNeighborsClassifier(n_neighbors=6)
    knn.fit(X_train, y_train)

    return knn

def retorna_previsao_knn(tabuleiro):
    knn = inicia_algoritmo()

    previsao = knn.predict(tabuleiro)
    
    return previsao