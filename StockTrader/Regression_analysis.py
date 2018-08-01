import numpy as np
import Parser
import Data_preprocessing as Dp
from sklearn import linear_model
import threading
import Regime_constructor
import Data_plotter


class Regression(threading.Thread):
    path_open = "C:\\Users\sandr\Documents\Financial_data\open\\"
    path_closed = "E:\Financial_data\closed\\"

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        self.regression()

    def regression(self):
        stock_data = Parser.parse_open(self.path_open + self.name)

        normalised_time = Dp.time_conversion(stock_data, time_interval='week', number=1)
        index_start = len(normalised_time)
        scaled_time = Dp.stock_regime_data_scale(normalised_time)
        stock_trade = Dp.stock_trade_normalisation(stock_data[1, -index_start:])
        stock_previous_close = Dp.stock_trade_normalisation(stock_data[3, -index_start:])
        stock_open = Dp.stock_trade_normalisation(stock_data[4, -index_start:])
        stock_day_high, stock_day_low = Dp.get_hig_and_low(stock_trade, normalised_time)
        #stock_day_high = Dp.stock_trade_normalisation(stock_day_high)
        #stock_day_low = Dp.stock_trade_normalisation(stock_day_low)
        returns = Dp.stock_trade_normalisation(stock_trade - np.roll(stock_trade, 2))
        df = np.array([stock_open, stock_day_high])
        regimes = Regime_constructor.regime_construct_1(np.reshape(df, (-1, df.shape[0])))

        Data_plotter.plot_regimes(np.asarray([normalised_time, returns, regimes]))


        length_of_normalised_time = len(normalised_time)
        start_index_stock_trade = len(stock_trade)-index_start
        reg = linear_model.LinearRegression()
        print(len(stock_trade[start_index_stock_trade:]), index_start)
        reg.fit([normalised_time],  stock_trade[start_index_stock_trade:])
        linear_model_coeffisient = reg.coef_
        print(linear_model_coeffisient)




    #def prepare_classes(self, ):





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

   # amd_object.start()
   # nvidia_object.start()
    micron_object.start()
    #alibaba_object.start()
    #netflix_object.start()
    #intel_object.start()

if __name__ == "__main__":
    main()