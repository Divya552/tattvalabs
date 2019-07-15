import pandas as pd
a=pd.read_csv('iris.data')
print(" dataset content")
print(a)
print("only starting 2 rows")
print(a.head(2)) #to print only starting 2 rows
print("only last 2 rows")
print(a.tail(2)) #to print only last 2 rows
print(a.describe())
print(" after excluding column, header and index ")
print(a.values)
print("AXes are:")
print(a.axes)
print("display all the target groups ")
print(a.groupby('Iris-setosa').groups)
