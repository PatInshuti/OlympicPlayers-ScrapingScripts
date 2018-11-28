import csv
from bs4 import BeautifulSoup #importing beautiful soup
import requests


url = "https://www.sports-reference.com/olympics/countries/FRA/"

#In order to send get request to the web -- we need to pass the url as a GET REQUEST
page_response = requests.get(url)
soup = BeautifulSoup(page_response.content, 'html.parser')
gamesInfo =  []

#Focus our search to only the " Year of games, Flag Bearer and Top medalists"
for tr in soup.find_all('tr')[1:]:
    column = tr.find_all('td')
    gamesInfo.append(column[1].text+","+column[2].text +","+column[11].text)

#Printing all information 
for i in range(len(gamesInfo)):
    print(gamesInfo[i])

#write in csv file called script2.csv
f = open('script2.csv','a')
for counter in range(len(gamesInfo)):
    f.write(str(gamesInfo[counter]))
    f.write('\n') #In order to write on a new line every loop
f.close()
