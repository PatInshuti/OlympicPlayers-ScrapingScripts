#import bs4
import csv
from bs4 import BeautifulSoup
import requests


url = "https://www.sports-reference.com/olympics/countries/FRA/"

#In order to send get request to the web -- we need to pass the url as a GET REQUEST
page_response = requests.get(url)
soup = BeautifulSoup(page_response.content, 'html.parser')

games =  []

#Focus our search to only the games, Flag Bearer and Top medalists

for tr in soup.find_all('tr')[2:]:
    tds = tr.find_all('td')
    #games.append(tds)
    games.append(tds[1].text+","+tds[2].text +","+tds[11].text)   

for i in range(len(games)):
    print(games[i])

#write in csv

f = open('file1.csv','w')
for counter in range(len(games)):
    f.write(str(games[counter]))
    f.write('\n')
    #Give your csv text here.
## Python will convert \n to os.linesep
f.close()
