
for i in list(data.columns):
    if type(data.loc[0,i])==str:
        print(i)
