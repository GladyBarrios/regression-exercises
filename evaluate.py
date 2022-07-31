import math
from sklearn.metrics import mean_squared_error

def plot_residuals(y, yhat):
    residuals = yhat - y
    plt.scatter(x=y, y=residuals)
    plt.title('Residual plot')    


 def regression_errors(y, yhat):
    sse = mean_squared_error(y, yhat) * len(y)
    ess = sum((yhat - y.mean()) ** 2)
    tss = sse + ess
    mse = mean_squared_error(y, yhat)
    rmse = math.sqrt(mse)
    return sse, ess, tss, mse, rmse  

def baseline_mean_errors(y):
    sse = mean_squared_error(y, y.mean()) * len(y)
    mse = mean_squared_error(y, y.mean())
    rmse = math.sqrt(mse)
    return sse, mse, rmse

 def better_than_baseline(y, yhat):
    sse = regression_errors(y, yhat)
    sse_b = baseline_mean_errors(y)
    if sse < sse_b:
        return True
    else:
        return False   