import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

# Umjetni podaci
np.random.seed(42)
X = np.random.rand(100, 2)
y = np.random.randint(0, 2, 100)

# a) Podjela (80-20, stratify)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

# b) Skaliranje (iako nije nužno za stablo)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# c) Model stabla odlučivanja
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_train_scaled, y_train)

# Predikcija
y_pred = dt.predict(X_test_scaled)

# d) Evaluacija
print("Matrica zabune:")
print(confusion_matrix(y_test, y_pred))

print("\nTočnost:", accuracy_score(y_test, y_pred))

print("\nIzvještaj klasifikacije:")
print(classification_report(y_test, y_pred))


# a) Vizualizacija stabla
plt.figure(figsize=(12, 8))
plot_tree(dt, filled=True, feature_names=["x1", "x2"], class_names=["0", "1"])
plt.show()
