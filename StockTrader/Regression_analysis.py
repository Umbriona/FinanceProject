import numpy as np
import Parser
import Data_preprocessing as Dp
from sklearn import linear_model
import threading


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
        stock_trade = stock_data[1, :]
        normalised_time = Dp.time_conversion(stock_data)
        length_of_normalised_time = len(normalised_time)
        start_index_stock_trade = len(stock_trade)-length_of_normalised_time
        reg = linear_model.LinearRegression()
        print(len(stock_trade[start_index_stock_trade:]), length_of_normalised_time)
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

    amd_object.start()
    nvidia_object.start()
    micron_object.start()
    alibaba_object.start()
    netflix_object.start()
    intel_object.start()

if __name__ == "__main__":
    main()