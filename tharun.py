
biased=['GarageType', 'GarageFinish', 'GarageQual', 'GarageCond','MSZoning','Condition1','RoofStyle']
datac = datac.drop(biased, axis = 1)


narrow=['EnclosedPorch','KitchenAbvGr']
datan = datan.drop(narrow, axis = 1)

z=['Street','Utilities','Condition2','RoofMatl','Heating','HeatingQC']
data = df2.drop(z,axis =1)
