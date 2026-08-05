import pandas as pd

df = pd.read_csv("C:\\Users\\Admin\\Desktop\\23CS141\\WiproPython\\MiniProj\\DatasetExample.csv")

print("Dataset:")
print(df)

numeric_data = df.select_dtypes(include=['int64', 'float64'])

Q1 = numeric_data.quantile(0.25)
Q3 = numeric_data.quantile(0.75)

IQR = Q3 - Q1

outliers = numeric_data[
    ((numeric_data < (Q1 - 1.5 * IQR)) |
     (numeric_data > (Q3 + 1.5 * IQR))).any(axis=1)
]

print("\nOutliers:")
print(outliers)

# O\P:
# Dataset:
#     ID  Age  Salary  Experience  Score
# 0    1   21   25000           1     75
# 1    2   22   27000           2     80
# 2    3   23   28000           2     78
# 3    4   24   30000           3     85
# 4    5   25   32000           4     82
# 5    6   26   35000           5     88
# 6    7   27   36000           5     90
# 7    8   28   38000           6     84
# 8    9   29   40000           7     86
# 9   10   30   42000           8     89
# 10  11   55  120000          25     95
# 11  12   20   24000           1     40

# Outliers:
#     ID  Age  Salary  Experience  Score
# 10  11   55  120000          25     95
# 11  12   20   24000           1     40
