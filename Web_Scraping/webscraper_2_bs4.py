from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://olympus.realpython.org/profiles/dionysus'
page = urlopen(url)  # opens the url
html = page.read().decode('utf-8')  # reads the page as a string
soup = BeautifulSoup(html, "html.parser")  # creates a BeautifulSoup object

print(soup.get_text())  # prints the text on the url website
img_list = soup.find_all("img")  # gets all the img tags and stores them in a list
print(img_list)
print(soup.title.string)  # prints the title as a string
