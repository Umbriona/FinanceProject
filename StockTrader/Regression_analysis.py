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

    def time_conversion(self, stock_data, time_interval = 'week'):
        length_stock_data = len(stock_data[0, :])
        stock_time = stock_data[]
        if time_interval == 'week':


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