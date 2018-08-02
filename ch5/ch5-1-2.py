from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
'''
@ JIN Yijie
'''

'''
Download all images in a webpage
'''

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html, "html.parser")
imageLocation = bsObj.find_all("a") # The type of imageLocation is <class 'bs4.element.Tag'>

# Store the URLs of all images in a set
# I don't use list beacuse list will somehow store all URLs as single characters 
# instead of URLs. 
# e.g.: list stores "http://www.pythonscraping.com" as ['h','t','t','p',':','/','/'...] 
# I am still trying to figure out the problem.
# I just figured out the problem. 
# If I use images+=[image["src"]], the URL of each image will be taken in as a whole.

# The URLs of images can be both stored in a set or a list.
# If they are stored in a set, we need to convert it to list at the urlretrieve step.
# If they are stored in a list, we need to add [] out of the image when add them to the list.

images = []
#images = set()
for i in range(len(imageLocation)):
    image = imageLocation[i].find("img")
    if image != None:
        if image not in images:
            # Note: It is neccessary to add [] out of image["src"], 
            # otherwise the list will take in the URL as separated letters. 
            images+=[image["src"]] 
            #images.add(image["src"]) # Needed if we use a set to store the URLs.s

for i in range(len(images)):
    # urlretrieve will store the images in current folder (the same as the code folder).
    urlretrieve(images[i], "logo"+str(i+1)+".jpg")

print("The program has finished.")