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






from sklearn.base import BaseEstimator, TransformerMixin
class MyLabelBinarizer(TransformerMixin):
    def __init__(self, *args, **kwargs):
        self.encoder = LabelBinarizer(*args, **kwargs)
    def fit(self, x, y=0):
        self.encoder.fit(x)
        return self
    def transform(self, x, y=0):
        return self.encoder.transform(x)
class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.attribute_names].values
from sklearn.pipeline import FeatureUnion
num_attribs = datan.columns
cat_attribs = datac.columns
num_pipeline = Pipeline([('selector', DataFrameSelector(num_attribs)),('imputer', SimpleImputer(strategy="median")),('std_scaler', StandardScaler()),])
cat_pipeline = Pipeline([('selector', DataFrameSelector(cat_attribs)),('label_binarizer', MyLabelBinarizer()),])
full_pipeline = FeatureUnion(transformer_list=[("num_pipeline", num_pipeline),("cat_pipeline", cat_pipeline),])
