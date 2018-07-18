import requests
from bs4 import BeautifulSoup
import time
import numpy as np
import threading


class Stock(threading.Thread):
    path_open = "E:\Financial_data\open\\"
    path_closed = "E:\Financial_data\closed\\"

    def __init__(self, url, filename):
        threading.Thread.__init__(self)
        self.page_url = url
        self.file_name = filename

    def run(self):
        while True:
            source_code = requests.get(self.page_url)
            plane_text = source_code.text
            soup = BeautifulSoup(plane_text, "html.parser")
            day = time.strftime("%a", time.gmtime())
            if time.localtime()[3] < 22 and time.localtime()[3] > 15 and (day != 'Sat' and day != 'Sun'):
                state = 'open'
            else:
                state = 'closed'

            title = ''

            if state == 'open':
                for link1 in soup.find_all('span', class_="Trsdu(0.3s)"):
                    title += link1.string + ' '
                fw = open(self.path_open + self.file_name + '_open.txt', 'a')
                tim = str(time.localtime()[3]) + ':' + str(time.localtime()[4]) + ':' + str(time.localtime()[5])
                date = str(time.localtime()[0]) + ':' + str(time.localtime()[1]) + ':' + str(time.localtime()[2])
                fw.write(title + tim + ' ' + date + '\n')
                fw.close()
                time.sleep(np.random.randint(300, 600))

            elif state == 'closed':
                for link1 in soup.find_all('span', class_="Trsdu(0.3s) "):
                    title += link1.string + ' '
                fw = open(self.path_closed + self.file_name + '_closed.txt', 'a')
                tim = str(time.localtime()[3]) + ':' + str(time.localtime()[4]) + ':' + str(time.localtime()[5])
                date = str(time.localtime()[0]) + ':' + str(time.localtime()[1]) + ':' + str(time.localtime()[2])
                fw.write(title + ' ' + tim + ' ' + date + '\n')
                fw.close()
                time.sleep(np.random.randint(1800, 2400))


def main():

    # file names
    amd_filename = "Amd"
    nvidia_filename = "Nvidia"
    micron_filename = "Micron"
    alibaba_filename = "Alibaba"
    netflix_filename = "Netflix"
    intel_filename = 'Intel'

    # Websites
    amd_url = "https://finance.yahoo.com/quote/AMD?p=AMD&guccounter=1"
    nvidia_url = "https://finance.yahoo.com/quote/NVDA?p=NVDA"
    micron_url = "https://finance.yahoo.com/quote/MU?p=MU"
    alibaba_url = "https://finance.yahoo.com/quote/BABA?p=BABA"
    netflix_url = "https://finance.yahoo.com/quote/NFLX?p=NFLX"
    intel_url = "https://finance.yahoo.com/quote/INTC?p=INTC"

    # Stock objects
    amd_object = Stock(amd_url, amd_filename)
    nvidia_object = Stock(nvidia_url, nvidia_filename)
    micron_object = Stock(micron_url, micron_filename)
    alibaba_object = Stock(alibaba_url, alibaba_filename)
    netflix_object = Stock(netflix_url, netflix_filename)
    intel_object = Stock(intel_url, intel_filename)

    amd_object.start()
    nvidia_object.start()
    micron_object.start()
    alibaba_object.start()
    netflix_object.start()
    intel_object.start()


if __name__ == "__main__":
    main()
