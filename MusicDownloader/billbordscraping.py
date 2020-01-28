from bs4 import BeautifulSoup 
import requests


class TopSongFind:
    def __init__(self):
        pass 

    def get_song_and_artist(self):
        url = 'https://www.billboard.com/charts/hot-100'
        source = requests.get(url).text 
        soup = BeautifulSoup(source , 'lxml')

        songs  = tuple(map( lambda item : item.get_text() ,soup.find_all('span' ,class_ = 'chart-element__information__song')))
        artist = tuple(map( lambda item : item.get_text() ,soup.find_all('span' ,class_ = 'chart-element__information__artist')))
        final = tuple(zip(songs , artist))
        return final

