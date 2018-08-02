from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html, "html.parser")
#imageLocation = bsObj.find("a", {"id": "logo"}).find("img")["src"]
#imageLocation = bsObj.find("a", {"id": "logo"})
imageLocation = bsObj.find_all("a")
print(type(imageLocation))
print(type(imageLocation[0]))


#print(type(imageLocation))
#print(len(imageLocation))

#urlretrieve(imageLocation, "logo.jpg")
print("The program has finished.")