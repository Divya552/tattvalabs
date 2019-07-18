import pandas as pd
df1=pd.DataFrame({
    'Name':['divya','bhavya','shaila','kumar','pooja','keerthi', 'lakshmi','kiran','surya','kala'],
    'USN':[1,2,3,4,5,6,7,8,9,10],
    'Sem':[4,6,8,4,5,7,7,8,4,5],
 'Branch':['ec','ec','ec','cs','ec','cs','is','cs','is','cs'],
'Score':[50,60,70,80,90,85,65,91,77,67],
'Region':['hubli','kumta','hubli','gadag','dharwad','kumta','bhatkal','kundapur','mangalore','hubli']
})
print(df1)
print(df1.describe())
print("the student who got maximum marks\n")
print(df1[df1['Score']==df1['Score'].max()])
#print(df1['Score'].mean())
print("the students who belonging to hubli region\n ")
print(df1[df1['Region']=='hubli'])
print("the students who belong to 7th sem\n")
print(df1[df1['Sem']==7])
#print(df1[['Name','USN']])
print(df1['Name'].str.capitalize())
print(df1.rename(index={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j'}))
