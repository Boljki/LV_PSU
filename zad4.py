import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# Umjetni podaci
np.random.seed(42)
X = np.random.rand(100, 2)
y = np.random.randint(0, 2, 100)

# a) Podjela
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

# b) Skaliranje (VAŽNO za logističku regresiju)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# c) Model logističke regresije
lr = LogisticRegression()
lr.fit(X_train, y_train)

# Predikcija
y_pred = lr.predict(X_test)

# d) Evaluacija
print("Matrica zabune:")
print(confusion_matrix(y_test, y_pred))

print("\nTočnost:", accuracy_score(y_test, y_pred))

print("\nIzvještaj klasifikacije:")
print(classification_report(y_test, y_pred))