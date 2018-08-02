from urllib.request import urlopen
from bs4 import BeautifulSoup   
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org'+pageUrl)
    bsObj = BeautifulSoup(html, 'html.parser')
    
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id='mw-content-text').find_all('p')[0])
        print(bsObj.find(id='ca-edit').find('span').attrs['href'])
    except AttributeError:
        print('This page is missing something! No worry though!')
    
        
    for link in bsObj.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # we encounter new pages
                newPage = link.attrs['href']
                print('----------------------\n'+newPage)
                #print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks('')