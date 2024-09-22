import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

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

y_pred = knn.predict(X_test)
# print(y_pred)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

y_pred = knn.predict([[2,0,1,0,2,1,0,1,1,1],
[2,0,1,0,2,1,2,2,1,1],
[2,0,1,0,2,0,1,1,1,3],
[2,0,1,2,1,1,1,0,0,3],
[2,0,1,2,1,1,0,0,1,1],
[2,0,1,2,1,0,1,1,0,3],
[2,0,1,2,1,0,1,0,1,3],
[2,0,1,2,1,0,1,2,2,3],
[2,0,1,2,1,2,1,0,2,3],
[2,0,1,2,1,2,1,2,0,3],
[2,0,1,2,0,1,0,1,1,1],
[2,0,1,2,0,1,2,2,1,1],
[2,0,1,2,0,0,1,1,1,3],
[2,0,1,2,2,1,0,2,1,1],
[2,0,1,2,2,1,2,0,1,1],
[2,0,0,1,1,1,1,0,2,3],
[2,0,0,1,1,1,1,2,0,3],
[2,0,0,1,1,1,0,1,2,3],
[2,0,0,1,1,1,0,2,1,3],
[2,0,0,1,1,1,2,1,0,3],
[2,0,0,1,1,1,2,0,1,3],
[2,0,0,1,1,1,2,2,2,3]])

# print(y_pred)