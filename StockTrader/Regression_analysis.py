import numpy as np
from StockTrader import Parser
import sklearn
import threading


class Regression(threading.Thread):
    path_open = "E:\Financial_data\open\\"
    path_closed = "E:\Financial_data\closed\\"

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        self.regression()

    def regression(self):
        stock_data = Parser.parse_open(self.path_open + self.name)
        stock_trade = stock_data[1, :]
        print(stock_data)
        normalised_time = self.time_conversion(stock_data)
        from sklearn import linear_model
        >> > reg = linear_model.LinearRegression()
        >> > reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
        LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
        >> > reg.coef_
        array([0.5, 0.5])

    def time_conversion(self, stock_data, time_interval='week', number=1):
        length_stock_data_0 = len(stock_data[:, 1])
        length_stock_data_1 = len(stock_data[0, :])
        stock_time = stock_data[length_stock_data_0 - 4, :]
        stock_date_year = stock_data[length_stock_data_0 - 3, :]
        stock_date_month = stock_data[length_stock_data_0 - 2, :]
        stock_date_day = stock_data[length_stock_data_0 - 1, :]

        if time_interval == 'week':
            month_days_arraay = np.array([31, 28, 30, 31, 30, 31, 30, 31, 30, 31, 30, 31])
            if self.is_leap_year(stock_date_year[length_stock_data_1-1]):
                month_days_arraay[1] = 29
            start_day = stock_date_day[length_stock_data_1-1]
            start_month = stock_date_month[length_stock_data_1-2]
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
                day = month_days_arraay[month-1]
            day = day - total_day_left
        # elif time_interval == 'month':
        condition = np.logical_and(np.equal(stock_data[length_stock_data_0 - 1, :], day),
                                   np.equal(stock_data[length_stock_data_0 - 2, :], month))
        index_day = np.amin(np.nonzero(condition))
        normalised_time = np.zeros(length_stock_data_1-index_day)
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
                normalised_time[start_indice:end_indice] = (stock_time[condition] - min_time_day) /\
                                                           (max_time_day - min_time_day) + np.amax(normalised_time) + 0.01
            day += 1
        return normalised_time

    def is_leap_year(self, year):
        """Determine whether a year is a leap year."""

        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def main():
    # file names
    amd_filename = "Amd_open.txt"
    nvidia_filename = "Nvidia_open.txt"
    micron_filename = "Micron_open.txt"
    alibaba_filename = "Alibaba_open.txt"
    netflix_filename = "Netflix_open.txt"
    intel_filename = 'Intel_open.txt'

    # Stock objects
    amd_object = Regression(amd_filename)
    nvidia_object = Regression(nvidia_filename)
    micron_object = Regression(micron_filename)
    alibaba_object = Regression(alibaba_filename)
    netflix_object = Regression(netflix_filename)
    intel_object = Regression(intel_filename)

    amd_object.start()
    nvidia_object.start()
    micron_object.start()
    alibaba_object.start()
    netflix_object.start()
    intel_object.start()

if __name__ == "__main__":
    main()