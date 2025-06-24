import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

file = "data/data.csv"
data = np.loadtxt(file, delimiter=',', skiprows=1)
x = data[:,0].reshape(-1,1)
y = data[:,1]
model = LinearRegression()
model.fit(x, y)

def prediction():
    pred = model.predict(x)
    return pred

def make_prediction():
    experience = float(input("Input your experience: "))
    pred = model.predict([[experience]])
    return experience, round(pred[0], 2)

def MSE():
    pred = model.predict(x)
    return round(mean_squared_error(y, pred), 2)

def MAE():
    pred = model.predict(x)
    return round(mean_absolute_error(y, pred), 2)
