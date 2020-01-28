from django.shortcuts import render , redirect 
from django.http import HttpResponse
import pafy , os , urllib.request
from bs4 import BeautifulSoup
from .billbordscraping import TopSongFind


def get_song_link(song_name):
    query = urllib.parse.quote(song_name)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    vid = soup.find(attrs={'class':'yt-uix-tile-link'})
    try:
        result = 'https://www.youtube.com' + vid['href']
    except:
        return HttpResponse('Enter correct detail')
    
    return result


def homepage(request):
    t1 = TopSongFind()
    song = t1.get_song_and_artist()
    index = tuple(range(100))
    song = list(zip(song,index))
    full_name = list(map(lambda item : item[0][0]+item[0][1] , song))
    context = { 'song': song , 'full_name' : full_name} 
    if request.method == 'POST':
        song_name = request.POST.get('song')
        song_link = get_song_link(song_name)
        try:
            down_ = pafy.new(song_link)
        except:
            return HttpResponse('Enter correct detail')
        audio = down_.audiostreams[-1]
        audio_link = audio.url + "&title=" + down_.title
        return redirect(audio_link)
    return render(request , 'MusicDownloader/home.html' , context)

def btndownload(request , value):
    song_link = get_song_link(value)
    down_ = pafy.new(song_link)
    audio = down_.audiostreams[-1]
    audio_link = audio.url + "&title=" + down_.title
    return redirect(audio_link)
    

def socialize(request):
    return render(request , 'MusicDownloader/aboutme.html')

