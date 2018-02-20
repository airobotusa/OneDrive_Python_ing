#https://www.youtube.com/watch?v=XQgXKtPSzUI
# Introduction To Web Scraping (with Python and Beautiful Soup)
# 1. from dos command, type "pip install bs4
# 2. type python
#>>> import bs4

import bs4
from urllib.request import urlopen as uReq

from bs4 import BeautifulSoup as soup

my_url ="https://arxiv.org/abs/1611.08754"
print("my_url is : ", my_url)

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
# html parser
page_soup = soup(page_html, "html.parser")
page_soup.h1

page_soup.p

page_soup.body.span

extraref= page_soup.findAll("div", {"class": "extra-ref-cite"})
print("len(extra-ref-cite) is ==> " , len(extraref))
len(extraref)

bookmark = page_soup.findAll("div", {"class": "bookmarks"})

book_marks = page_soup.findAll("div", {"class": "bookmarks"})
print("len(extra-ref-cite) is ==> " , len(extraref))
bookmarkk = bookmark[0]

bookmarkk.a
bookmarkk.div

# good example with list
lists_all = page_soup.findAll("div", {"class": "list"})
print("len(list_all) is : ==> ", len(lists_all))
listall = lists_all[0]




