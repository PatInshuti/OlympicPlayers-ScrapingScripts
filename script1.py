from bs4 import BeautifulSoup  #importing beautiful soup
import requests

url = "https://www.ranker.com/list/famous-female-athletes-from-france/reference"
#In order to send get request to the web -- we need to pass the url as a "GET" REQUEST
page_response = requests.get(url)
soup = BeautifulSoup(page_response.content, 'html.parser')

listPlayers =  []
listPlayers2 = []
#Focus our search to only the names

for playerNames in soup.find_all('a',attrs={"class":"listItem__title"}):
    listPlayers.append(str(playerNames.text))

for playerNames in soup.find_all('h2',attrs={"class":"listItem"}):
    listPlayers2.append(str(playerNames.text))


print(listPlayers)
print(len(listPlayers))

print(len(listPlayers2))
print(listPlayers2)
