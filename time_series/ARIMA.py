from pandas import read_csv
import datetime
from matplotlib import pyplot

def parser(x):
    return datetime.strptime()

def initialPlot(input_file):
    series = read_csv(input_file)
    print(series.head())
    series.plot()
    pyplot.show()

if __name__ == "__main__":
    input_file = "PM25_ARIMA.csv"
    initialPlot(input_file)