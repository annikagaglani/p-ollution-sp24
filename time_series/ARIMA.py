from pandas import read_csv
from datetime import datetime
from matplotlib import pyplot

def parser(x):
    return datetime.strptime(x, '%m/%d/%Y')

def initialPlot(input_file):
    series = read_csv(input_file, header=0, parse_dates=[0], index_col=0, date_parser=parser)
    print(series.head())
    series.plot()
    pyplot.show()

if __name__ == "__main__":
    input_file = "PM25_ARIMA.csv"
    initialPlot(input_file)