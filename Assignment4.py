import pandas as pd
d=pd.DataFrame({
    'Book Name': ['Data Structures','Introduction to algorithms','Design Patterns','Code Complete','Artificial Intelligence','Compilers','Algorithm Design','Java','Code Book','File Structures'],
'Author Name': ['Padmareddy','Thomas','Erich gamma','Steve','Stuart','Alfred','jon','Alex','Simon','Micheal']
})
print(d)
name=input("enter the ending letter of author name")
print(d[d['Author Name'].str.endswith(name)])
name1=input("enter the starting letter of author name")
print(d[d['Author Name'].str.startswith(name1)])
