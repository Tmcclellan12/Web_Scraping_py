##Scrapes AOC website "housing as a human right"
##Exports a text file w/ data 

import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.ocasiocortez.com/issues#housing-as-a-human-right")
soup = BeautifulSoup(page.content,'html.parser')
mylist = soup.find_all(class_="issue-footnotes")

lis = []
for ul in mylist:
    for li in ul.findAll('li'):
        if li.find('ul'):
            break
        lis.append(li)

for li in lis: 
    print (li.text.encode("utf-8"))
