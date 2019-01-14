from bs4 import BeautifulSoup  #importing beautiful soup
import requests

url = "https://www.ranker.com/list/famous-female-athletes-from-france/reference"
#In order to send get request to the web -- we need to pass the url as a "GET" REQUEST
page_response = requests.get(url)
soup = BeautifulSoup(page_response.content, 'html.parser')

listPlayers =  []
listPlayers2 = []
#Focus our search to only the names

# for playerNames in soup.find_all('div',attrs={"class":["listItem__data","listItem__title--link"]}):
#     listPlayers.append(str(playerNames.text))

for playerNames in soup.find_all('div',attrs={"class":"listItem__data"}):
    listPlayers2.append(str(playerNames.text))

# True, {"class":["class1", "class2"]}

print(listPlayers2)
print(len(listPlayers2))

# a class="listItem__title listItem__title--link black"

# class="listItem__title--link listItem__h2Link black listItem__title"