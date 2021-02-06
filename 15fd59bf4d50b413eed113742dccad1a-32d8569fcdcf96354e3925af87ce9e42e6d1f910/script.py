import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/honeyproduction.csv")
regr = linear_model.LinearRegression()
prod_per_year = df.groupby('year').totalprod.mean().reset_index()
X = prod_per_year.year.values.reshape(-1,1)
y = prod_per_year.totalprod.values
regr.fit(X,y)
y_predict = regr.predict(X)
plt.scatter(X,y)
plt.plot(X,y_predict)
plt.ylabel('Total Production per year')
plt.xlabel('Year')
plt.title('Average Production per Year')
plt.show()

X_future = np.array(range(2013,2055))
X_future = X_future.reshape(-1,1)
future_predict = regr.predict(X_future)
plt.plot(X_future, future_predict)
plt.show()