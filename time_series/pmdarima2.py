import pmdarima as pm
from pmdarima.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv

# Read in file and parse dates
def parser(x):
    return datetime.strptime(x, '%m/%d/%Y')
series = read_csv(input_file, header=0, parse_dates=[0], index_col=0, date_parser=parser)

# Split data
train_size = int(len(series) * 0.66)
train, test = train_test_split(series, train_size)

# Fit model
model = pm.auto_arima(train, seasonal=True, m=365)

# Forecasts
forecasts = model.predict(test.shape[0])

# Visualize the forecasts (blue=train, green=forecasts)
x = np.arrange(series.shape[0])
plt.plot(x[:150], train, c='blue')
plt.plot(x[150:], forecasts, c='green')
plt.show()

if __name__ == "__main__":
    input_file = "PM25_ARIMA.csv"
    initialPlot(input_file)


    
