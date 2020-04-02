for i in a:
    print(data[i].value_counts())

    
z=['Street','Utilities','Condition2','RoofMatl','Heating','HeatingQC']
datac=pd.DataFrame(data[a],columns=a)
print(datac.head())

for i in z:
    datac.drop(i,axis=1)
for i in a: 
    data.drop(i,axis=1)
