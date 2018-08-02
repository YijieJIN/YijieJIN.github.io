from urllib.request import urlopen
from bs4 import BeautifulSoup   
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# Retrieve a list of all internal links found on a page
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # Find all links that begin with a '/'
    for link in bsObj.find_all('a', href=re.compile('^(/|.*'+includeUrl+')')):
        if link.attrs['href'] not in internalLinks:
            internalLinks.append(link.attrs['href'])
    return internalLinks

# Retrieve a list of all enternal links found on a page
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # Find all links that start with 'http' or 'www' that do not contain the curren URL
    for link in bsObj.find_all('a', href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
        if link.attrs['href'] not in externalLinks:
            externalLinks.append(link.attrs['href'])
    return externalLinks
        
def splitAddress(address):
    '''
    Delete 'http://' in the URL and split it by '/'
    e.g.: 
    input: http://www.stats.gov.cn/tjsj/pcsj/rkpc/6rp/indexch.htm
    return: ['www.stats.gov.cn', 'tjsj', 'pcsj', 'rkpc', '6rp', 'indexch.htm'] (data type: list)
    '''
    addressParts = address.replace('http://', '').split('/')
    #print('The type of addressParts is: '+str(type(addressParts)))
    return addressParts

def getRandomExternalLink(startingPage):
    '''
    Search for links until we find an external link.
    
    The logic is like this:
    
    Do we have an external link? 
    
    if yes:
        return that external link
    else:
        find the first internal link
    Repeat this process until we finally find an external link
    '''
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, 'html.parser')
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0]) 
    # splitAddress(startingPage) returns a list, 
    # we need to choose an element in the list so that the input of getExternalLinks will be a string
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(bsObj, splitAddress(startingPage)[0])
        return getExternalLinks(bsObj, internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingPage, count):
    externalLink = getRandomExternalLink(startingPage)
    print(str(count)+": Random external link is: "+externalLink)
    count+=1
    followExternalOnly(externalLink, count)

#followExternalOnly("http://oreilly.com", 0)
html = urlopen("http://oreilly.com")
bsObj = BeautifulSoup(html, 'html.parser')

list = getInternalLinks(bsObj, '')
count = 1
for i in range(len(list)):
    print(str(count)+": "+list[count-1])
    count+=1
print("-----------------------------------------")


#print(splitAddress("http://oreilly.com"))
print("-------------------------")
list = getExternalLinks(bsObj, splitAddress("http://oreilly.com")[0])
#print(len(list))
count = 1
for i in range(len(list)):
    print(str(count)+": "+list[count-1])
    count+=1
print("-----------------------------------------")

# collect all external links on the page
allIntLinks = set()
allExtLinks = set()
def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
    externalLinks = getExternalLinks(bsObj, splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            print("The next URL to get is: "+link)
            allIntLinks.add(link)
            getAllExternalLinks(link)

getAllExternalLinks("http://oreilly.com")