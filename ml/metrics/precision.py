# Use this as a metric for BINARY CLASSIFICATION only
import numpy as np


def precision(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    tp, fp, tn, fn = 0, 0, 0, 0
    if len(y_true) == len(y_pred):
        for i in range(len(y_true)):
            if y_true[i] == 1 and y_pred[i] == 1:
                tp += 1
            elif y_true[i] == 1 and y_pred[i] == 0:
                fn += 1
            elif y_true[i] == 0 and y_pred[i] == 0:
                tn += 1
            else:
                fp += 1
    else:
        print("The lengths of the arrays dont match!!!\nCheck the arrays again")
    precision = tp / (tp + fp)
    return precision


# Testing the metric
if __name__ == '__main__':
    y_true = [1, 0, 1, 1, 1, 0, 1]
    y_pred = [1, 1, 0, 0, 0, 0, 0]
    precision = precision(y_true, y_pred)
    print(precision)
