"""
    File name: data_processing.py
    Author: Łukasz Jędryczka
    Date created: 06/12/2018
    Python Version: 3.6

    Processing data
"""
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np
import math

import warnings

warnings.filterwarnings(action="ignore", module="sklearn", message="^internal gelsd")


def smooth_data(data, return_all=False):
    """
    Smoothing data with linear regression, mean or moving average value
    :param data: data we want to smooth
    :param return_all: if we want more approximations then linear regression
    :return: smoothed data
    """
    in_data = np.array([i for i in range(len(data))])
    in_data = in_data.reshape(-1, 1)
    data = np.array(data)
    out_data = data[np.logical_not(np.isnan(data))]
    out_data = out_data.reshape(-1, 1)
    if not len(out_data):
        return np.array([0] * len(data))
    in_c_data = in_data[np.logical_not(np.isnan(data))]
    in_c_data = in_c_data.reshape(-1, 1)
    classifier = LinearRegression()
    classifier.fit(in_c_data, out_data)
    predict = classifier.predict(in_c_data)
    r2 = r2_score(out_data, predict)
    linear_predict = classifier.predict(in_data)
    mean_fill = replace_nan_with_mean(data)
    moving_average = replace_nan_with_moving_average(data)
    moving_w_average = replace_nan_with_moving_average(data, weights=True)
    linear_replacing = replace_nan_data(data, linear_predict)
    if return_all:
        return linear_replacing, linear_predict.flatten(), r2, mean_fill, moving_average, moving_w_average
    return linear_replacing


def linear_regression(data):
    """
    Calculating linear regression for data
    :param data: input data
    :return: linear regression
    """
    in_data = np.array([i for i in range(len(data))])
    in_data = in_data.reshape(-1, 1)
    data = np.array(data)
    out_data = data[np.logical_not(np.isnan(data))]
    out_data = out_data.reshape(-1, 1)
    if not len(out_data):
        return np.array([0] * len(data))
    in_c_data = in_data[np.logical_not(np.isnan(data))]
    in_c_data = in_c_data.reshape(-1, 1)
    classifier = LinearRegression()
    classifier.fit(in_c_data, out_data)
    return classifier.predict(in_data)


def replace_nan_data(base_data, replacing_data):
    """
    Replacing NaN values of data
    :param base_data: data to fill
    :param replacing_data: data we want to replace with
    :return: data with replaced values
    """
    x_data = np.array(base_data)
    y_data = np.array(replacing_data)
    for idx, d in enumerate(x_data):
        if math.isnan(d):
            x_data[idx] = y_data[idx]
    return x_data


def replace_nan_with_mean(data):
    """
    Replace NaN values with mean value
    :param data: data we want to fill
    :return: data with replaced values
    """
    result = np.array(data)
    mean = np.nanmean(data)
    indexes = np.where(np.isnan(data))
    result[indexes] = mean
    return result


def replace_nan_with_moving_average(data, weights=False):
    """
    Replace data with moving average value
    :param data:
    :param data:
    :param weights:
    :return: data with replaced values
    """
    result = np.array(data)
    if math.isnan(result[0]):
        result[0] = np.nanmean(result)
    for idx, d in enumerate(result):
        if math.isnan(d):
            avg = 0
            w = 0
            for i in range(idx):
                ms = result[i]
                if weights:
                    ms *= (i + 1)
                    w += (i + 1)
                avg += ms
            if weights and w is not 0:
                result[idx] = avg / w
            elif not weights and idx is not 0:
                result[idx] = avg / idx
    return result
