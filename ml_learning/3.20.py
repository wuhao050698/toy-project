# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 11:49
# @Author  : wu
# @FileName: 3.20.py
# @Project: testPyTorch
# 最小二乘法矩阵形式实现（easy）
import pandas as pd
import numpy as np
from sklearn import linear_model

df=pd.read_csv('C:/Users/asus/Desktop/PRSA_data_2010.1.1-2014.12.31.csv')
df = df.dropna()
# print(df.head())
df.loc[df['cbwd']=='SE','cbwd'] = 0
df.loc[df['cbwd']=='cv','cbwd'] = 1
df.loc[df['cbwd']=='NW','cbwd'] = 2
df.loc[df['cbwd']=='NE','cbwd'] = 3
df = np.array(df)
#print(df[:,0:5])
#   第5列是pm2.5
X=np.mat(np.delete(df,[0,5],axis=1))
Y=df[:,5]
X = X[1:2000,:]
Y = Y[1:2000]
b=(np.dot(X.T,X)).I
b=np.dot(np.dot(b,X.T),Y)
print(b)
model = linear_model.LinearRegression()
model.fit(X, Y)
print(model.coef_)
