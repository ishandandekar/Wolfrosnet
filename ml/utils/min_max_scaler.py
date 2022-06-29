from cmath import inf
import numpy as np


class MinMaxScaler:
    def __init__(self):
        return None

    def fit(self, arr):
        self.mini = min(arr)
        self.maxi = max(arr)

    def transform(self, arr):
        if self.maxi == inf:
            raise ValueError(
                "Value of max_imum is infinity. Scaled values cannot be computed")
        if self.mini == -inf:
            raise ValueError(
                "Value of min_imum is infinity. Scaled values cannot be computed")
        if self.mini == self.maxi:
            raise ValueError("Values of max_imum and min_imum is the same ")
        if self.mini > min(arr):
            raise ValueError(
                "The array on which the scaler is fitted has greater minimum. Scaled values cannot be computed")
        if self.maxi < max(arr):
            raise ValueError(
                "The array on which the scaler is fitted has lower maximum. Scaled values cannot be computed")
        scaled_arr = []
        for value in arr:
            scaled_value = float((value-self.mini)/(self.maxi-self.mini))
            scaled_arr.append(scaled_value)
        return scaled_arr

    def fit_transform(self, column):
        array = np.array(column)
        self.fit(array)
        return self.transform(array)


def main():
    arr_1 = [1, 2, 3, 4, 5, 6]
    scaler = MinMaxScaler()
    scaler.fit(arr_1)
    arr_2 = [2, 3, 4, 4, 6]
    print(scaler.transform(arr_2))


if __name__ == "__main__":
    main()
