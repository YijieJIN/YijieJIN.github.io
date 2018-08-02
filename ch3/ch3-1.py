from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

# use the current time to generate a random seed each time run the program, 
# which promises that we can get a totally different random path each time.
# Note that the same seed will generate the same pseudo random number
random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    '''
    Read in the URL of the article. Return the links inside the wiki page
    ''' 
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, 'html.parser')
    return bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks("/wiki/Kevin_Bacon")
# If the length of the links is not 0, randomly print out a link until the length of the links is 0. 
while len(links)>0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)

