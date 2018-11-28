#import bs4
from bs4 import BeautifulSoup
import requests


url = "https://www.ranker.com/list/famous-female-athletes-from-france/reference"

#In order to send get request to the web -- we need to pass the url as a GET REQUEST
page_response = requests.get(url)
soup = BeautifulSoup(page_response.content, 'html.parser')

listPlayers =  []

listPlayers2= []
#Focus our search to only the names
#<a class="listItem__title listItem__title--link black" rel="follow" itemprop="url" href="//www.ranker.com/review/mary-pierce/1536141?ref=node_name&amp;pos=1&amp;a=0&amp;ltype=n&amp;l=557823&amp;g=1">Mary Pierce</a>

for playerNames in soup.find_all('a',attrs={"class":"listItem__title"}):
    listPlayers.append(str(playerNames.text))

for playerNames in soup.find_all('h2',attrs={"class":"listItem"}):
    listPlayers2.append(str(playerNames.text))


print(listPlayers)

print(len(listPlayers))

print(len(listPlayers2))
print(listPlayers2)
