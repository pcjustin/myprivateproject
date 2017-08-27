__author__= 'Justin Lu'

from urllib import request
from bs4 import BeautifulSoup as bs

def getNowPlayingMovieList():
    resp = request.urlopen('https://movie.douban.com/nowplaying/shenzhen/')
    html_data = resp.read().decode('utf-8')
    soup = bs(html_data, 'html.parser')
    nowplaying_movies = soup.find_all('div', id='nowplaying')
    nowplaying_movie_list = nowplaying_movies[0].find_all('li', class_='list-item')
    nowplaying_lists = []
    for item in nowplaying_movie_list:
        nowplaying_dict = {}
        nowplaying_dict['id'] = item['data-subject']
        nowplaying_dict['name'] = item['data-title']
        for img_item in item.find_all('img'):
            nowplaying_dict['img'] = img_item['src']
            nowplaying_lists.append(nowplaying_dict)

    return nowplaying_lists

def getMoiveRatingById(movieId):
    resp = request.urlopen('https://movie.douban.com/subject/' + movieId + '/?from=playing_poster')
    html_data = resp.read().decode('utf-8')
    soup = bs(html_data, 'html.parser')
    rating = soup.find_all('div', typeof='v:Rating')
    try:
        average = rating[0].find_all('strong', property='v:average')
        if average[0].string == None:
            return 0
    except:
        return 0

    return float(average[0].string)

def main():
    NowPlayingMovieList = getNowPlayingMovieList()
    NowPlayingMoiveRatingList = []
    for NowPlayingMoive in NowPlayingMovieList:
        NowPlayingMoiveRatingDict = {}
        NowPlayingMoiveRatingDict['name'] = NowPlayingMoive['name']
        NowPlayingMoiveRatingDict['img'] = NowPlayingMoive['img']
        NowPlayingMoiveRatingDict['rating'] = getMoiveRatingById(NowPlayingMoive['id'])
        NowPlayingMoiveRatingList.append(NowPlayingMoiveRatingDict)

    NowPlayingMoiveRatingList.sort(key=lambda k: (k.get('rating', 0)), reverse=True)
    for idx, r in enumerate(NowPlayingMoiveRatingList):
        print('name: ' +  r['name'] + ' rating: ' + str(r['rating']) + ' img: ' + r['img'])


if __name__ == '__main__':
    main()
