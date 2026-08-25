#Mini proj 2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle

df = pd.read_csv("Diabetes.csv")

print("--- DATASET OVERVIEW ---")
df.info()

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DESCRIPTIVE STATISTICS ---")
print(df.describe())

df.dropna(inplace=True)

plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="Blues")
plt.title("Feature Correlation Heatmap")

plt.subplot(1, 2, 2)
target_col = df.columns[8] if df.shape[1] > 8 else df.columns[-1]
sns.countplot(x=df[target_col])
plt.title("Target Distribution (" + str(target_col) + ")")

plt.tight_layout()
plt.show()

features = df.iloc[:, 0:8].values
label = df.iloc[:, 8].values

x_train, x_test, y_train, y_test = train_test_split(
    features, label, test_size=0.2, random_state=23
)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)

train_pred = model.predict(x_train)
test_pred = model.predict(x_test)

train_accuracy = accuracy_score(y_train, train_pred)
test_accuracy = accuracy_score(y_test, test_pred)

print("\n--- MODEL ACCURACY & PERFORMANCE ---")
print("Train Accuracy:", train_accuracy)
print("Test Accuracy: ", test_accuracy)

print("\n--- CONFUSION MATRIX ---")
print(confusion_matrix(y_test, test_pred))

print("\n--- CLASSIFICATION REPORT ---")
print(classification_report(y_test, test_pred))

with open("Diabetes_KNN.model", "wb") as f:
    pickle.dump(model, f)
print("\nModel successfully saved to Diabetes_KNN.model")
