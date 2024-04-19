import sys
from pandas import read_csv, DataFrame
from datetime import datetime
from pandas.plotting import autocorrelation_plot
from matplotlib import pyplot
from statsmodels.tsa.arima.model import ARIMA

def parser(x):
    return datetime.strptime(x, '%m/%d/%Y')

def initialSummary():
    print(series.head())

def initialPlot():
    series.plot()  # Removing the last 4 characters (.csv)
    pyplot.legend([input_file[:-10]])
    pyplot.savefig('aqi.jpg')
    pyplot.show()

def autoCorr():
    autocorrelation_plot(series)
    pyplot.legend([input_file[:-10]]) # TODO: make the legend show the blue line
    pyplot.savefig('correlation.jpg')
    pyplot.show()

def arimaSummary():
    print(model_fit.summary())

def arimaResiduals():
    residuals.plot()
    pyplot.legend([input_file[:-10]])
    pyplot.savefig('residuals.jpg')
    pyplot.show()
    
def arimaDensity():
    residuals.plot(kind='kde')
    pyplot.legend([input_file[:-10]])
    pyplot.savefig('density.jpg')
    pyplot.show()

def arimaResidualsSummary():
    residuals = DataFrame(model_fit.resid)
    print(residuals.describe())




if __name__ == "__main__":
    available_functions = ['initialSummary', 'initialPlot', 'autoCorr', 'arimaSummary', 'arimaResiduals', 'arimaDensity', 'arimaResidualsSummary'] 

    if len(sys.argv) < 3:
        print("Usage: python file.py <file> <function>")
        print(f"Available functions: {', '.join(available_functions)}")
        sys.exit(1)
    
    input_file = sys.argv[1] # TODO: set this up for so2
    function_name = sys.argv[2]

    series = read_csv(input_file, header=0, parse_dates=[0], index_col=0, date_parser=parser)
    series.index = series.index.to_period('M')

    model = ARIMA(series, order=(5,1,0))
    model_fit = model.fit()
    residuals = DataFrame(model_fit.resid)
    
    if function_name not in available_functions:
        print("Function '{}' not found. Available functions: {}".format(function_name, ", ".join(available_functions)))
        sys.exit(1)

    getattr(sys.modules[__name__], function_name)()
