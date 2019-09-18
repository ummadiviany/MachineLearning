import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, cross_validation, svm

data = pd.read_csv('feed.csv')
#print(data)
data = data[['field4']]
#print(data)
forecast_out = int(30)
data['Prediction'] = data[['field4']].shift(-forecast_out)
print(data)
X = np.array(data.drop(['Prediction'], 1))
X = preprocessing.scale(X)
X_forecast = X[-forecast_out:]
X = X[:-forecast_out]
y = np.array(data['Prediction'])
y = y[:-forecast_out]
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.2)

l = LinearRegression()
l.fit(X_train,y_train)

forecast_prediction = l.predict(X_forecast)
print(forecast_prediction)
fig = plt.figure()
ax1 = fig.add_subplot(111)
line1 = ax1.plot(forecast_prediction)
plt.show()
