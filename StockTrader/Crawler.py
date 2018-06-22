import requests
from bs4 import BeautifulSoup

def stoc_spider(max_pages):
    page=1
    while page<=max_pages:
       page_url =r' https: // query1.finance.yahoo.com / v7 / finance / download / AMD?period1 = 1526841548 & period2 = 1529519948 & interval = 1d & events = history & crumb = w9QCQ2KTsHt'
