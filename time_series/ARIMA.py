from pandas import read_csv
from datetime import datetime
from matplotlib import pyplot
from pandas import DataFrame
from statsmodels.tsa.arima.model import ARIMA

def parser(x):
    return datetime.strptime(x, '%m/%d/%Y')

def initialPlot(input_file):
    # Load dataset
    series = read_csv(input_file, header=0, parse_dates=[0], index_col=0, date_parser=parser)
    print(series.head())
    series.plot()
    pyplot.show()
    series.index = series.index.to_period('M')

    # Fit Model
    model = ARIMA(series, order=(5,1,0))
    model_fit = model.fit()

    # summary of fit model
    print(model_fit.summary())

    # line plot of residuals
    residuals = DataFrame(model_fit.resid)
    residuals.plot()
    pyplot.show()

    #density plot of residuals
    residuals.plot(kind='kde')
    pyplot.show()

    #summary stats of residuals
    print(residuals.describe())



if __name__ == "__main__":
    input_file = "PM25_ARIMA.csv"
    initialPlot(input_file)