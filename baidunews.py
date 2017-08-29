__author__= 'Justin Lu'

from urllib import request
from bs4 import BeautifulSoup as bs


def getfocusnews(focusnews):
    for news in focusnews.find_all('a'):
        print(news.string + ' ' + news['href'])


def getfocuslistnews(soup):
    focuslistnews = soup.find_all('ul', class_='ulist focuslistnews')
    for focusnews in focuslistnews:
        getfocusnews(focusnews)


def gethotlistnews(soup):
    hotnews = soup.find_all('strong')
    for news in hotnews:
        print(news.find('a').string + ' ' + news.find('a')['href'])


def getNewsLists():
    resp = request.urlopen("http://news.baidu.com/")
    html_data = resp.read().decode('utf-8')
    soup = bs(html_data, 'html.parser')
    gethotlistnews(soup)
    getfocuslistnews(soup)


def main():
    getNewsLists();

if __name__ == '__main__':
    main()