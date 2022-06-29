import numpy as np


def root_mean_squared_error(y_true, y_pred):
    return np.sqrt(np.mean((np.array(y_true)-np.array(y_pred))**2))


# Testing the metric
if __name__ == '__main__':
    y_true = [0, 1, 2, 3, 4, 5]
    y_predicted = [0, 0.96, 1.68, 3.05, 4.89, 4.98]
    rmse = root_mean_squared_error(y_true=y_true, y_pred=y_predicted)
    print(f"Mean sqaured error: {rmse}")
