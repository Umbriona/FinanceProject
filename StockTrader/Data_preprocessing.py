import numpy as np
from sklearn import preprocessing


def time_conversion(stock_data, time_interval='week', number=1):
    length_stock_data_0 = len(stock_data[:, 1])
    length_stock_data_1 = len(stock_data[0, :])
    stock_time = stock_data[length_stock_data_0 - 4, :]
    stock_date_year = stock_data[length_stock_data_0 - 3, :]
    stock_date_month = stock_data[length_stock_data_0 - 2, :]
    stock_date_day = stock_data[length_stock_data_0 - 1, :]

    if time_interval == 'week':
        month_days_arraay = np.array([31, 28, 30, 31, 30, 31, 30, 31, 30, 31, 30, 31])
        if is_leap_year(stock_date_year[length_stock_data_1 - 1]):
            month_days_arraay[1] = 29
        start_day = stock_date_day[length_stock_data_1 - 1]
        start_month = int(stock_date_month[length_stock_data_1 - 2])
        total_day = 7 * number
        day = start_day
        month = start_month
        total_day_left = total_day
        while day < total_day_left:
            total_day_left = total_day_left - day
            if month == 1:
                month = 12
            else:
                month -= 1
            day = month_days_arraay[month - 1]
        day = day - total_day_left
    # elif time_interval == 'month':
    condition = np.logical_and(np.equal(stock_data[length_stock_data_0 - 1, :], day),
                               np.equal(stock_data[length_stock_data_0 - 2, :], month))
    index_day = np.amin(np.nonzero(condition))
    normalised_time = np.zeros(length_stock_data_1 - index_day)
    while day <= np.amax(stock_date_day):
        condition = np.logical_and(np.equal(stock_data[length_stock_data_0 - 1, :], day),
                                   np.equal(stock_data[length_stock_data_0 - 2, :], month))
        if np.any(condition):
            index_day_min = np.amin(np.nonzero(condition))
            index_day_max = np.amax(np.nonzero(condition))
            min_time_day = stock_time[index_day_min]
            max_time_day = stock_time[index_day_max]
            start_indice = np.amin(np.where(normalised_time == 0))
            end_indice = np.count_nonzero(condition) + start_indice
            normalised_time[start_indice:end_indice] = (stock_time[condition] - min_time_day) / \
                                                       (max_time_day - min_time_day) + np.amax(normalised_time) + 0.0001
        day += 1
    return normalised_time


def is_leap_year(year):
    """Determine whether a year is a leap year."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def stock_trade_normalisation(stock_trade):
    stock_trade_min = np.amin(stock_trade)
    stock_trade_max = np.amax(stock_trade)
    return (stock_trade - stock_trade_min) / (stock_trade_max - stock_trade_min)


def stock_regime_data_scale(stock_regime_data):
    scaled_data = preprocessing.scale(stock_regime_data, axis=0)
    return scaled_data


def get_hig_and_low(data, time_vec):
    max_time = int(np.trunc(np.amax(time_vec)))
    vec_max = np.zeros(np.shape(data))
    vec_min = np.zeros(np.shape(data))
    previous_time = 0
    for i in range(max_time):
        time = (i+1+(i+1)*0.0001)
        condition = np.logical_and(np.greater(time_vec, previous_time), np.less_equal(time_vec, time))
        vec_max[condition] = np.amax(data[condition])
        vec_min[condition] = np.amin(data[condition])
        previous_time = time
    return vec_max, vec_min




