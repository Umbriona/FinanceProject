import requests
from bs4 import BeautifulSoup
import threading


class Market(threading.Thread):

    def __init__(self, market_name, sead_url):
        self.market_name = market_name
        self.url = sead_url

    def run(self):
        source_code = requests.get(self.page_url)
        plane_text = source_code.text
        soup = BeautifulSoup(plane_text, "html.parser")