from pandas import read_csv
from datetime import datetime
from matplotlib import pyplot
from pandas import DataFrame
from statsmodels.tsa.arima.model import ARIMA
import warnings
from math import sqrt
from sklearn.metrics import mean_squared_error

# Evaluate ARIMA model with certain params
def evaluate_arima_model(X, arima_order):
    # Training dataset
    train_size = int(len(X) * 0.66)
    train, test = X[0:train_size], X[train_size:]
    history = [x for x in train]

    # Make predictions 
    predictions = list()
    for t in range(len(test)):
        model = ARIMA(history, order= arima_order)
        model_fit = model.fit()
        yhat = model_fit.forecast()[0]
        predictions.append(yhat)
        history.append(test[t])

    # Calculate out sample error?
    rmse = sqrt(mean_squared_error(test, predictions))
    return rmse

def evaluate_models(dataset, p_values, d_values, q_values):
    dataset = dataset.astype('float32')
    best_score, best_cfg = float("inf"), None
    for p in p_values:
        for d in d_values:
            for q in q_values:
                order = (p,d,q)
                try:
                    rmse = evaluate_arima_model(dataset, order)
                    if rmse < best_score:
                        best_score, best_cfg = rmse, order
                        print('ARIMA%s RMSE=%.3f' % (order,rmse))
                except:
                    continue
                    print('Best ARIMA%s RMSE=%.3f' % (best_cfg, best_score))

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

def evalParams(input_file):
    series = read_csv(input_file, header=0, parse_dates=[0], index_col=0, date_parser=parser)
    p_values = [0, 1, 2, 4, 6, 8, 10]
    d_values = range(0, 3)
    q_values = range(0, 3)
    warnings.filterwarnings("ignore")
    evaluate_models(series.values, p_values, d_values, q_values)

if __name__ == "__main__":
    input_file = "PM25_ARIMA.csv"
    initialPlot(input_file)