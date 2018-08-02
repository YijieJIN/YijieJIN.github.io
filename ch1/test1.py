from urllib.request import urlopen
from bs4 import BeautifulSoup

'''
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(),'lxml')
print(bsObj.h1)
'''

'''
try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
    # return null, break the program or execute another option
try:
'''

def getTitle(url):
    '''
    Since we may encounter many exceptions due to internet connection,
    it is much safer to use try catch block to deal with exceptions
    '''
    try:
        html = urlopen(url) # open the url to the object html
    except HTTPError as e:
        print(e)
        return None
    try: 
        bsObj = BeautifulSoup(html.read(),'lxml')
        print(bsObj.find("nonExistentTag")) # eprint None
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:   
    print("Title could not be found")
else:
    print(title)