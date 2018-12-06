from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np
import math

import warnings

warnings.filterwarnings(action="ignore", module="sklearn", message="^internal gelsd")


def smooth_data(in_data, out_data):
    if len(in_data) is not len(out_data):
        raise AttributeError(f'X ({len(input)}) and Y ({len(out_data)}) data lengths must be equal')

    y_data = np.array(out_data)
    classifier = LinearRegression()
    indexes = []
    for idx, d in enumerate(y_data):
        if math.isnan(d):
            indexes.append(idx)
    x_data = np.delete(in_data, indexes)
    x_data = x_data.reshape(-1, 1)
    y_data = [d for d in y_data if not math.isnan(d)]
    y_data = np.asarray(y_data)
    y_data = y_data.reshape(-1, 1)
    classifier.fit(x_data, y_data)

    predict = classifier.predict(x_data)
    r2 = r2_score(y_data, predict)

    # if r2 > 0.9:
    linear_predict = classifier.predict(in_data.reshape(-1, 1))
    return replace_nan_data(out_data, linear_predict), linear_predict.flatten(), r2


def replace_nan_data(base_data, replacing_data):
    x_data = np.array(base_data)
    y_data = np.array(replacing_data)
    for idx, d in enumerate(x_data):
        if math.isnan(d):
            x_data[idx] = y_data[idx]
    return x_data
