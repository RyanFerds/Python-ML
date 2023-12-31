# -*- coding: utf-8 -*-
"""Linear regressiondj.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B0RsbtYWGJLtl_cKTnj9W9RxaKVOm4Ri
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x=np.random.rand(100,1)
y = 2 + 3 * x + np.random.rand(100, 1)
plt.scatter(x,y,s=10)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
model=LinearRegression()
model.fit(x,y)
pred=model.predict(x)
mse=mean_squared_error(pred,y)
plt.plot(x,pred,color='red')
plt.scatter(x, y, s=10)
plt.xlabel('x')
plt.ylabel('y')

plt.show()
print(mse)

data=pd.read_csv("/content/Fuel.xls")

data.head()

data = data[["ENGINESIZE","CO2EMISSIONS","CYLINDERS"]]

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
n=100
ax.scatter(data["ENGINESIZE"],data["CO2EMISSIONS"],data["CYLINDERS"],color="red")
ax.set_xlabel("ENGINESIZE")
ax.set_ylabel("CO2EMISSIONS")
ax.set_zlabel("CYLINDERS")
plt.show()

train = data[:(int((len(data)*0.8)))]
test = data[(int((len(data)*0.8))):]

regr =LinearRegression()
train_x = np.array(train[["ENGINESIZE"]])
train_y = np.array(train[["CO2EMISSIONS"]])
regr.fit(train_x,train_y)

ax.scatter(data["ENGINESIZE"],data["CO2EMISSIONS"],data["CYLINDERS"],color="red")
plt.plot(train_x, regr.coef_*train_x + regr.intercept_, '-r')
ax.set_xlabel("ENGINESIZE")
ax.set_ylabel("CO2EMISSIONS")
ax.set_zlabel("CYLINDERS")

def get_regression_predictions(input_features,intercept,slope):
    predicted_values = input_features*slope + intercept
    return predicted_values


from sklearn.metrics import r2_score
test_x = np.array(test[['ENGINESIZE']])
test_y = np.array(test[['CO2EMISSIONS']])
test_y_ = regr.predict(test_x)
print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Mean sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y)** 2))
print("R2-score: %.2f" % r2_score(test_y_ , test_y) )