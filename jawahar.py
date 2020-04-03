import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
data=pd.read_csv('../input/house-prices-advanced-regression-techniques/train.csv')
data.dropna(axis=1,thresh=1000,inplace=True)
narrow=['PoolArea','3SsnPorch','EnclosedPorch','BsmtFinSF2','BsmtHalfBath','KitchenAbvGr','LowQualFinSF','MiscVal','ScreenPorch']
for i in narrow:
    data.drop(i,inplace=True,axis=1)
dtype=data.dtypes
mask=(dtype=='object')
datac=pd.DataFrame(columns=None)
masked=dtype[mask]
for i in list(masked.index):
    datac[i]=data[i]
    data.drop(i,axis=1,inplace=True)
biased=['Street','GarageType', 'GarageFinish', 'GarageQual', 'GarageCond','MSZoning','Condition1','RoofStyle']
datac.drop(biased,axis=1,inplace=True)
