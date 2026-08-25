#Ass 2
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

dataset = pd.read_csv("50_Startups.txt", comment = '#')

print("--- First 5 Rows of the Dataset ---")
print(dataset.head())
print("\n" + "=" * 50 + "\n")

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

ct = ColumnTransformer(
    transformers=[("encoder", OneHotEncoder(), [3])], remainder="passthrough"
)
X = np.array(ct.fit_transform(X))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("--- Actual vs Predicted Profits (Test Set) ---")
comparison_df = pd.DataFrame(
    {"Actual Profit": y_test, "Predicted Profit": np.round(y_pred, 2)}
)
print(comparison_df)
print("\n" + "=" * 50 + "\n")

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("--- Evaluation Metrics ---")
print(f"1. Mean Absolute Error (MAE):     ${mae:,.2f}")
print(f"2. Mean Squared Error (MSE):      ${mse:,.2f}")
print(f"3. Root Mean Squared Error (RMSE): ${rmse:,.2f}")
print(f"4. R-squared Score (R²):           {r2:.4f} ({r2 * 100:.2f}%)")
