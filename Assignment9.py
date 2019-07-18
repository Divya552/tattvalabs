import pandas as pd

df=pd.read_csv('student.csv')
print(df)
#print(df['Score'].max())
#print(df['Score'].mean())
#print(df[df['Region']=='hubli'])
#print(df)

print(df.describe())
print("the student who got maximum marks\n")

print(df[df['Score']==df['Score'].max()])
#print(df1['Score'].mean())
print("the students who belonging to hubli region\n ")
print(df[df['Region']=='hubli'])
print("the students who belong to 6th sem\n")
print(df[df['Sem']==6])
print(df[['Name','USN']])
print(df['Name'].str.capitalize())
print(df.rename(index={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j'}))
