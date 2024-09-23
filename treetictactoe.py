from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

def inicia_algoritmo():
    data = pd.read_csv('./tic-tac-toe-processed.data', sep=',', header=0)

    X = data
    y = data['result']

    # aumentar tamanho do teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

    tree = DecisionTreeClassifier()

    tree.fit(X_train, y_train)
    
    return tree

def retorna_previsao_tree(tabuleiro):
    tree = inicia_algoritmo()

    previsao = tree.predict(tabuleiro)

    return previsao