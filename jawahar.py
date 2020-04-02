
for i in list(data.columns):
    if type(data.loc[0,i])==str:
        print(i)

a = [i for i in list(df2.columns) if type(df2.loc[0,i])==str]
print(a)   
