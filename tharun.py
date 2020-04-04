# %% [code]
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Any results you write to the current directory are saved as output.

# %% [code]
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline

# %% [code]
df = pd.read_csv("../input/house-prices-advanced-regression-techniques/train.csv")


# %% [code]
df1 = df.drop(["Alley","FireplaceQu","PoolQC","Fence","MiscFeature"], axis = 1)

# %% [code]


# %% [code]


# %% [code]


# %% [code]
corm = df1.corr()
corm["SalePrice"].sort_values(ascending = False)

# %% [code]
df2 = df1.drop(["ScreenPorch",    "PoolArea","MoSold",          "3SsnPorch",       "BsmtFinSF2",  "BsmtHalfBath" ,   "MiscVal"       ,  "Id"    ,          "LowQualFinSF" ,    "YrSold"  ,        "OverallCond"],axis = 1)

# %% [code]


# %% [code]


# %% [code]


# %% [code]


# %% [code]
count = 0
a = [i for i in list(df2.columns) if type(df2.loc[0,i])==str]
print(a)   
        

# %% [code]




# %% [code]
for i in a:
    print(df2[i].value_counts())


# %% [code]
z=['Street','Utilities','Condition2','RoofMatl','Heating','HeatingQC']
data = df2.drop(z,axis =1)

# %% [code]
z=['Street','Utilities','Condition2','RoofMatl','Heating','HeatingQC']
datac=pd.DataFrame(df2[a],columns=a)

# %% [code]
datac = datac.drop(z,axis = 1)

# %% [code]
datan = df2.drop(a,axis = 1)



# %% [code]

from sklearn.preprocessing import StandardScaler

# %% [code]


# %% [code]



# %% [code]


# %% [code]

# %% [code]




# %% [code]




# %% [code]
narrow=['EnclosedPorch','KitchenAbvGr']
datan = datan.drop(narrow, axis = 1)








# %% [code]
from sklearn.pipeline import Pipeline

# %% [code]
from sklearn.pipeline import FeatureUnion

# %% [code]
num_attribs = list(datan)
biased=['GarageType', 'GarageFinish', 'GarageQual', 'GarageCond','MSZoning','Condition1','RoofStyle']
datac = datac.drop(biased, axis = 1)

# %% [code]
cat_attribs = list(datac)
from sklearn.preprocessing import LabelBinarizer

# %% [code]


# %% [code]


# %% [code]



# %% [code]
dataall = pd.concat([datac,datan], sort = False)



# %% [code]


# %% [code]

# %% [code]







# %% [code]

# %% [code]

# %% [code]


# %% [code]
from sklearn.impute import SimpleImputer
from sklearn.pipeline import FeatureUnion
num_attribs = list(datan)
cat_attribs = list(datac)
num_pipeline = Pipeline([
('selector', DataFrameSelector(num_attribs)),
('imputer', SimpleImputer(strategy="median")),
('std_scaler', StandardScaler()),
])
cat_pipeline = Pipeline([
('selector', DataFrameSelector(cat_attribs)),
('label_binarizer', LabelBinarizer()),
])
full_pipeline = FeatureUnion(transformer_list=[
("num_pipeline", num_pipeline),
("cat_pipeline", cat_pipeline),
])

from sklearn.base import BaseEstimator, TransformerMixin
class DataFrameSelector(BaseEstimator, TransformerMixin):
 def __init__(self, attribute_names):
  self.attribute_names = attribute_names
 def fit(self, X, y=None):
  return self
 def transform(self, X):
  return X[self.attribute_names].values

