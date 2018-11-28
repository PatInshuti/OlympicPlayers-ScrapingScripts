#import bs4
from bs4 import BeautifulSoup
import requests

#We put all the urls in a list so that we can loop through the list (Each list has it's own alphabets of Names) IDK if this makes sense lol :)
listUrls = ["https://en.wikipedia.org/w/index.php?title=Category%3AOlympic_athletes_of_France","https://en.wikipedia.org/w/index.php?title=Category:Olympic_athletes_of_France&pagefrom=Courtejaire%2C+Leon%0AL%C3%A9on+Courtejaire#mw-pages", "https://en.wikipedia.org/w/index.php?title=Category:Olympic_athletes_of_France&pagefrom=Guillouet%2C+Marcel%0AMarcel+Guillouet#mw-pages",
"https://en.wikipedia.org/w/index.php?title=Category:Olympic_athletes_of_France&pagefrom=Montebrun%2C+Manuela%0AManuela+Montebrun#mw-pages", "https://en.wikipedia.org/w/index.php?title=Category:Olympic_athletes_of_France&pagefrom=Ugolini%2C+Gerard%0AG%C3%A9rard+Ugolini#mw-pages"]

players =  []
for links in listUrls:
    #In order to send get request to the web -- we need to pass the url as a GET REQUEST
    page_response = requests.get(links)
    soup = BeautifulSoup(page_response.content, 'html.parser')
    

    #Focus our search to only the names only by letter categorization
    for playerNames in soup.find_all('div',attrs={"class":"mw-category-group"}):
        players.append(str(playerNames.text))

for i in range(len(players)):
    print(players[i])

#write in csv file called script3.csv
f = open('script3.csv','a')
for counter in range(len(players)):
    f.write(str(players[counter]))
    f.write('\n') #In order to write on a new line every loop
f.close()