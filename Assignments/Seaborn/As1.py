import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

mallData = pd.read_csv("MallData.csv")

print("Info:")
print(mallData.info())
print()

print("Missing Values:")
print(mallData.isnull().sum())
print()

print("Describe:")
print(mallData.describe())
print()

sns.heatmap(mallData.corr(numeric_only = True), annot = True)
plt.title("Market Analysis")

plt.show()

# O/P:
# Info:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 40 entries, 0 to 39
# Data columns (total 5 columns):
#  #   Column                  Non-Null Count  Dtype 
# ---  ------                  --------------  ----- 
#  0   CustomerID              40 non-null     int64 
#  1   Gender                  40 non-null     object
#  2   Age                     40 non-null     int64 
#  3   Annual Income (k$)      40 non-null     int64 
#  4   Spending Score (1-100)  40 non-null     int64 
# dtypes: int64(4), object(1)
# memory usage: 1.7+ KB
# None

# Missing Values:
# CustomerID                0
# Gender                    0
# Age                       0
# Annual Income (k$)        0
# Spending Score (1-100)    0
# dtype: int64

# Describe:
#        CustomerID        Age  Annual Income (k$)  Spending Score (1-100)
# count   40.000000  40.000000           40.000000               40.000000
# mean    20.500000  35.450000           54.950000               50.450000
# std     11.690452  11.167604           24.290918               32.050401
# min      1.000000  19.000000           15.000000                3.000000
# 25%     10.750000  29.000000           38.500000               16.500000
# 50%     20.500000  33.500000           66.500000               49.500000
# 75%     30.250000  40.500000           74.250000               81.500000
# max     40.000000  64.000000           80.000000               97.000000
