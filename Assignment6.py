import pandas as pd
df=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data")
print(df)
print("only starting 2 rows")
print(df.head(2)) #to print only starting 2 rows
print("only last 2 rows")
print(df.tail(2)) #to print only last 2 rows
print(df.describe())
print(" after excluding column, header and index ")
print(df.values)
print("AXes are:")
print(df.axes)
print("display all the target groups with their  values")
print(df.groupby('1').groups)
