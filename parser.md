# poetry-research-project

import urllib
from BeautifulSoup import *

url = raw_input("Enter: ")

html  = urllib.urlopen(url).read()
soup = BeautifulSoup(html)