from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,'html.parser')


# dealing with children tags
for child in bsObj.find("table", {"id":"giftList"}).children:
    print(child)

# dealing with sibling tags
for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)

# dealing with parent tags
''' 
the parent tag of src is td, 
previous_sibing returns the previous tag, 
which contains the price of the good in the picture
'''
print(bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())


# re.compile compiles regular strings
images = bsObj.find_all("img", {"src": re.compile("\.\.\/img/\gifts/img.*\.jpg")})
for image in images:
    # print the src of images
    print(image["src"])