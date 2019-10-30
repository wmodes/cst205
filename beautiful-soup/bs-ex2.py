from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
# import pysound;

# Use the web page you chose here:
# my_site = "https://freesound.org/"
my_site = "https://freesound.org/"
my_page = "https://freesound.org/people/FunWithSound/sounds/416704/"
req = Request(my_page, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req)

soup = BeautifulSoup(html.read(), 'html.parser')

# print("Title", soup.title)
# featured_sound_div = soup.find(id="featured_sound")
featured_sound_div = soup.find(id="single_sample_player")
# print(featured_sound_div)

filename_div = featured_sound_div.find('div',{'class': 'metadata'})
# print(filename_div)
filename_link = filename_div.find('a',{'class': 'mp3_file'})
# print(filename_link)
print(my_site + filename_link['href'])

# print(soup.prettify())
