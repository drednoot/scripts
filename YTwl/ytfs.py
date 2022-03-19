from bs4 import BeautifulSoup as bs
import sys
from os import environ

home = environ['HOME']
path = home + "/.cache/ytfs/page.html"

with open(path) as file:
    soup = bs(file, 'html.parser')
    
    # format: [ (link, title, author) ]
    titles = []
    
    playlist = soup.find('ytd-playlist-video-list-renderer').find(id="contents")
    for item in playlist.find_all("ytd-playlist-video-renderer"):
        meta = item.find(id="meta")
        atag = meta.h3.a
        author = meta.find(class_="playlist style-scope ytd-playlist-video-renderer").find("a").get_text()
        link = "https://youtube.com" + atag.attrs["href"]
        title = atag.get_text()
        # remove all the unnecessary whitespaces
        title = " ".join(title.split())
        titles.append((link, title, author))

file.close()

with open(home + '/.cache/ytfs/temp', 'w') as file:
    for link, title, author in titles:
        file.write(link + ' ' + title + ' | ' + author + '\n')
