import requests
from bs4 import BeautifulSoup
import datetime
import schedule
import time
import numpy as np

def stock_spider(state = 'open'):
    page_url = r'https://finance.yahoo.com/quote/AMD?p=AMD&guccounter=1'
    source_code = requests.get(page_url)
    plane_text = source_code.text
    soup = BeautifulSoup(plane_text, "html.parser")

    filename_open = ''
    filename_closed = ''
    title = ''
    if state == 'open':
        for link1 in soup.find_all('span', class_="Trsdu(0.3s)"):
            title += link1.string + ' '
        fw = open('w', filename_open)
        fw.write(title + '\n')
        fw.close()

    elif state == 'closed':
        for link1 in soup.find_all('span', class_="Trsdu(0.3s) "):
            title += link1.string + ' '
        fw = open('w', filename_closed)
        fw.write(title + '\n')
        fw.close()


def job_stock_exchange_opening():
    while time.localtime()[3] < 22:
        if time.localtime()[4]%10:
            time.sleep(np.randomint(100))
            stock_spider('open')


def job_stock_exchange_closing():
    while time.localtime()[3] > 22 or time.localtime()[3] < 15:
        if time.localtime()[4] % 29:
            time.sleep(np.randomint(100))
            stock_spider('closed')


def main():
    struct_time = time.localtime()
    print(struct_time[3])
    schedule.every().monday.at("15:30").do(job_stock_exchange_opening())
    schedule.every().tuesday.at("15:30").do(job_stock_exchange_opening())
    schedule.every().wednesday.at("15:30").do(job_stock_exchange_opening())
    schedule.every().thursday.at("15:30").do(job_stock_exchange_opening())
    schedule.every().friday.at("15:30").do(job_stock_exchange_opening())

    schedule.every().monday.at("22:00").do(job_stock_exchange_closing())
    schedule.every().tuesday.at("22:00").do(job_stock_exchange_closing())
    schedule.every().wednesday.at("22:00").do(job_stock_exchange_closing())
    schedule.every().thursday.at("22:00").do(job_stock_exchange_closing())
    schedule.every().friday.at("22:00").do(job_stock_exchange_closing())


if __name__ == "__main__":
    main()
