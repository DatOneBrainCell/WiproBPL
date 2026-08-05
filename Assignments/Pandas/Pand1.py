import pandas as pd

cols = ["Mpg", "Cylinders", "Displacement", "HorsePower", "Weight", "Acceleration", "ModelYear", "Origin", "CarName"]

df = pd.read_csv("Cars.csv")
df.columns = cols

print(df.head(10))

print(df["CarName"])

print(df.tail())

print(df.info())

# O\P:
#     Mpg  Cylinders  Displacement HorsePower  Weight  Acceleration  ModelYear  Origin              CarName
# 0  15.0          8         350.0      165.0  3693.0          11.5         70       1    buick skylark 320
# 1  18.0          8         318.0      150.0  3436.0          11.0         70       1   plymouth satellite
# 2  16.0          8         304.0      150.0  3433.0          12.0         70       1        amc rebel sst
# 3  17.0          8         302.0      140.0  3449.0          10.5         70       1          ford torino
# 4  15.0          8         429.0      198.0  4341.0          10.0         70       1     ford galaxie 500
# 5  14.0          8         454.0      220.0  4354.0           9.0         70       1     chevrolet impala
# 6  14.0          8         440.0      215.0  4312.0           8.5         70       1    plymouth fury iii
# 7  14.0          8         455.0      225.0  4425.0          10.0         70       1     pontiac catalina
# 8  15.0          8         390.0      190.0  3850.0           8.5         70       1   amc ambassador dpl
# 9  15.0          8         383.0      170.0  3563.0          10.0         70       1  dodge challenger se
# 0       buick skylark 320
# 1      plymouth satellite
# 2           amc rebel sst
# 3             ford torino
# 4        ford galaxie 500
#               ...        
# 392       ford mustang gl
# 393             vw pickup
# 394         dodge rampage
# 395           ford ranger
# 396            chevy s-10
# Name: CarName, Length: 397, dtype: str
#       Mpg  Cylinders  Displacement HorsePower  Weight  Acceleration  ModelYear  Origin          CarName
# 392  27.0          4         140.0      86.00  2790.0          15.6         82       1  ford mustang gl
# 393  44.0          4          97.0      52.00  2130.0          24.6         82       2        vw pickup
# 394  32.0          4         135.0      84.00  2295.0          11.6         82       1    dodge rampage
# 395  28.0          4         120.0      79.00  2625.0          18.6         82       1      ford ranger
# 396  31.0          4         119.0      82.00  2720.0          19.4         82       1       chevy s-10
# <class 'pandas.DataFrame'>
# RangeIndex: 397 entries, 0 to 396
# Data columns (total 9 columns):
#  #   Column        Non-Null Count  Dtype  
# ---  ------        --------------  -----  
#  0   Mpg           397 non-null    float64
#  1   Cylinders     397 non-null    int64  
#  2   Displacement  397 non-null    float64
#  3   HorsePower    397 non-null    str    
#  4   Weight        397 non-null    float64
#  5   Acceleration  397 non-null    float64
#  6   ModelYear     397 non-null    int64  
#  7   Origin        397 non-null    int64  
#  8   CarName       397 non-null    str    
# dtypes: float64(4), int64(3), str(2)
# memory usage: 28.0 KB
# None
