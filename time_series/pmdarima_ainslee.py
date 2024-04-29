import pmdarima as pm
from pmdarima.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv, DataFrame
from datetime import datetime
import joblib

print("hi idiot")

# Read in file and parse dates
input_file = "monthly_pm25.csv"
def parser(x):
    return datetime.strptime(x, '%m/%d/%Y')
pm_series = read_csv(input_file, header=0)
print("read done")

# Split data
train_size = int(len(pm_series) * 0.66)
pm_X = pm_series[['Year']]
pm_y = pm_series['Average_AQI']
X_train, X_test, y_train, y_test = train_test_split(pm_X, pm_y, test_size=0.33)
print("train test split done")

# Fit model
model = pm.auto_arima(y_train, seasonal=True, m=12)
print("model fit done")

# Save model
joblib.dump(model, 'arima_model.pkl')
print("model saved")

# Forecasts
forecasts = model.predict(y_test.shape[0])
print("forecasts done")

# Save forecasts
np.save('forecasts.npy', forecasts)
print("forecasts saved")

# Visualize the forecasts (blue=train, green=forecasts)
print("visualizing...")
x = np.arange(pm_y.shape[0])
plt.plot(x[:len(y_train)], y_train, c='blue')
plt.plot(x[len(y_train):], forecasts, c='green')
plt.savefig('monthly_pm25_forecasts.png')
