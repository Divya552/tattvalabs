import pandas as pd
import json
#f2=open('student.json')
df=pd.read_json("student.json")

print("the json file contents are:\n",df)
df.to_csv('results.csv')
d=pd.read_csv("results.csv")
print("the csv file contents are\n",d)
