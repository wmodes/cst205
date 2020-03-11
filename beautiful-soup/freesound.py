from urllib.request import urlopen
from bs4 import BeautifulSoup 
import webbrowser

# Use the web page you chose here:
site = "https://freesound.org"
# html = urlopen(site) 

# this is for me since my machine is broken
with open("freesound.html", "r") as file:
	html = file.read();

# print(html)

# for folks w out a broken cert
# soup = BeautifulSoup(html.read(), 'html.parser')
# for me
soup = BeautifulSoup(html, 'html.parser')

# print (soup.prettify())

# get featured_sound block
featured_sound_html = soup.find(id="featured_sound")

# find <div> with class 'sound_title'
title_block_html = featured_sound_html.find('div', {"class": "sound_title"})
# find <a> tag with class 'title'
title_html = title_block_html.find('a', {'class': 'title'})
# get 'title' attribute from <a> tag
title = title_html["title"]

# get metadata div
metadata_html = featured_sound_html.find('div', {"class": "metadata"})
# get mp3 file from that
mp3_html = metadata_html.find('a', {"class": "mp3_file"})
# get href attr
url = site + mp3_html['href']

print (title)
print(url)
webbrowser.open(url)