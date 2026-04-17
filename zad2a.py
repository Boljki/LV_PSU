import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# Generiranje umjetnih podataka
np.random.seed(42)
X = np.random.rand(100, 2)
y = np.random.randint(0, 2, 100)

# a) Podjela (80% train, 20% test, stratify)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

# b) Skaliranje
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# c) KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)

# Predikcija
y_pred = knn.predict(X_test_scaled)

# d) Evaluacija

#   a) matrica zabune
print("Matrica zabune:")
print(confusion_matrix(y_test, y_pred))

#   b) točnost
print("\nTočnost:", accuracy_score(y_test, y_pred))

#   c) preciznost i odziv
print("\nIzvještaj klasifikacije:")
print(classification_report(y_test, y_pred))


# e) Utjecaj broja susjeda
print("\nUtjecaj broja susjeda:")
for k in [1, 3, 5, 10, 20]:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train_scaled, y_train)
    y_pred_k = model.predict(X_test_scaled)
    print(f"k = {k}, točnost = {accuracy_score(y_test, y_pred_k)}")


# f) Bez skaliranja
knn_no_scale = KNeighborsClassifier(n_neighbors=3)
knn_no_scale.fit(X_train, y_train)
y_pred_no_scale = knn_no_scale.predict(X_test)

print("\nTočnost bez skaliranja:", accuracy_score(y_test, y_pred_no_scale))


