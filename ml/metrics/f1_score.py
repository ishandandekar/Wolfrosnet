# Use this as a metric for BINARY CLASSIFICATION only
import numpy as np


def f1_score(y_true, y_pred):
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
    recall = tp/(tp+fn)
    f1_score = 2*precision*recall/(precision+recall)
    return f1_score


# Testing the metric
if __name__ == '__main__':
    from sklearn import metrics
    y_true = [1, 0, 1, 1, 1, 0, 1]
    y_pred = [1, 1, 0, 1, 1, 1, 0]
    f1_score = f1_score(y_true, y_pred)
    f1_score_sklearn = metrics.f1_score(y_true, y_pred)
    print(
        f"f1_score using the above function: {f1_score}\nf1_score using sklearn: {f1_score_sklearn}")
