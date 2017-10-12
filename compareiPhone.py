__author__= 'Justin Lu'

import json
import re
from urllib import request
from bs4 import BeautifulSoup as bs


def getPrice(country):
    url = "https://www.apple.com/" + country + "/shop/buy-iphone/iphone-8/"
    resp = request.urlopen(url)
    html_data = resp.read().decode('utf-8')
    soup = bs(html_data.lower(), 'html.parser')
    url_data = soup.script.string
    for item in json.loads(url_data)['offers']:
        sku = item['sku']
        if (re.search('mq6', sku)):
            price = item['price']
            pricecurrency = item['pricecurrency']
            print(sku + ": " + str(price) + " " + pricecurrency)


if __name__ == '__main__':
    getPrice('hk-zh')
    getPrice('cn')
    getPrice('tw')