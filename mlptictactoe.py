from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

def inicia_algoritmo_mlp():
    data = pd.read_csv('./tic-tac-toe-processed.data', sep=',', header=0)

    X = data
    y = data['result']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.fit_transform(X_test)

    mlp = MLPClassifier(hidden_layer_sizes=(4, 2), max_iter=1000, random_state=42)

    mlp.fit(X_train, y_train)

    return mlp

def retorna_previsao_mlp(tabuleiro, mlp):
    previsao = int(mlp.predict(tabuleiro)[0])
    
    if (previsao == 0):
        return 0
    elif (previsao == 1):
        return 1
    elif (previsao == 2):
        return 2
    elif (previsao == 3):
        return 3