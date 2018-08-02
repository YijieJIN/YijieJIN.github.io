from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import re
import random

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    '''
    Return all wikipedia links in the body part of the page
    articleUrl should be in this form: /wiki/Python_(programming_language) 
    (without https://en.wikipedia.org because we would append the predix in the program)
    '''

    html = urlopen("https://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, 'html.parser')
    return bsObj.find("div", {"id": "bodyContent"}).find_all("a", href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
    '''
    Return all anonymous users' IP addresses in history page
    '''
    # Format of history pages is:
    # https://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    # We are looking for URLs with the same format

    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "https://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"
    print("The first history URL is: "+historyUrl)

    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, "html.parser")

    # Find only the links with class "mw-anonuserlink" 
    # which has IP addresses instead of usernames

    ipAddresses = bsObj.find_all("a", {"class": "mw-anonuserlink"})
    print(type(ipAddresses))
    addressList = set()
    for ipAddress in ipAddresses:
        if addressList not in addressList:
            addressList.add(ipAddress.get_text())
    return addressList 

# test getLinks
links = getLinks("/wiki/Python_(programming_language)")
#print(type(links)) # Output: <class 'bs4.element.ResultSet'>
#print(type(links[1])) # Output: <class 'bs4.element.Tag'>


while (len(links)>0):
    for link in links:
        print("-------------------------------")
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            print(historyIP)


newLink = links[random.randint(0, len(links)-1)].attrs["href"]
# newLink is a random link chosen from links
print(newLink)
links = getLinks(newLink)
for i in range(10):
    # print out the contents in the first ten links
    print(links[i].get_text())



# test getHistoryIPs
addressList = getHistoryIPs("/wiki/Python_(programming_language)")
print(type(addressList))
print(len(addressList))
for i in range(len(addressList)):
    print("The "+str(i+1)+"-th IP address is: "+str(list(addressList)[i]))
