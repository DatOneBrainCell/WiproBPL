#Mini proj 1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pickle

df = pd.read_csv("Advertise.csv")

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
sns.histplot(df[target_col], kde=True, color="skyblue")
plt.title("Target Distribution (" + str(target_col) + ")")

plt.tight_layout()
plt.show()

features = df.iloc[:, [1, 2, 3, 4]].values
label = df.iloc[:, [8]].values

x_train, x_test, y_train, y_test = train_test_split(
    features, label, test_size=0.2, random_state=23
)

model = LinearRegression()
model.fit(x_train, y_train)

train_pred = model.predict(x_train)
test_pred = model.predict(x_test)

train_accuracy = model.score(x_train, y_train)
test_accuracy = r2_score(y_test, test_pred)

print("\n--- MODEL ACCURACY & PERFORMANCE ---")
print("Train Accuracy (R2 Score):", train_accuracy)
print("Test Accuracy (R2 Score): ", test_accuracy)
print("MAE (Test):               ", mean_absolute_error(y_test, test_pred))
print("RMSE (Test):              ", np.sqrt(mean_squared_error(y_test, test_pred)))

print("\n--- COEFFICIENTS & INTERCEPT ---")
print("Coefficients:", model.coef_)
print("Intercept:   ", model.intercept_)

with open("AdEffectiveness.model", "wb") as f:
    pickle.dump(model, f)
print("\nModel successfully saved to AdEffectiveness.model")
