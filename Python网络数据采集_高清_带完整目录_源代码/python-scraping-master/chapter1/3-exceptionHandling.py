from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys




def getTitle(url):
    ''' 
    Since we may encounter many exceptions due to internet connection,
    it is much safer to use try catch block to deal with exceptions
    '''
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        print(bsObj.nonExistentTag)
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
    
    