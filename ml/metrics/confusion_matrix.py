# Use this as a metric for BINARY CLASSIFICATION only
import numpy as np


def confusion_matrix(y_true, y_pred):
    conf_mat = np.zeros((2, 2))
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
    conf_mat[0][0] = tp
    conf_mat[0][1] = fn
    conf_mat[1][0] = fp
    conf_mat[1][1] = tn
    return np.matrix(conf_mat)


# Testing the metric
if __name__ == '__main__':
    import seaborn as sns
    import matplotlib.pyplot as plt
    y_true = [1, 0, 1, 1, 1, 0, 1]
    y_pred = [1, 1, 0, 1, 1, 1, 0]
    cm = confusion_matrix(y_true, y_pred)
    print(cm)
    sns.heatmap(cm, annot=True, fmt=".0f", cmap="Blues")
    plt.show()
