from bs4 import BeautifulSoup as bs
import sys
from os import environ

home = environ['HOME']
path = home + "/.config/ytfs/.path"
with open(path) as file:
    path = file.read()

with open(path) as file:
    soup = bs(file, 'html.parser')
    
    # format: [ (link, title) ]
    titles = []
    
    playlist = soup.find('ytd-playlist-video-list-renderer').find(id="contents")
    for item in playlist.find_all("ytd-playlist-video-renderer"):
        atag = item.find(id="meta").h3.a
        link = atag.attrs["href"]
        title = atag.get_text()
        # remove all the unnecessary whitespaces
        title = " ".join(title.split())
        titles.append((link, title))

file.close()

with open(home + '/.config/ytfs/.temp', 'w') as file:
    for link, title in titles:
        file.write(link + ' ' + title + '\n')
