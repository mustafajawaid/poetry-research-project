from requests import get
from bs4 import BeautifulSoup as BS
response = get('https://www.rekhta.org/ghazals/hazaaron-khvaahishen-aisii-ki-har-khvaahish-pe-dam-nikle-mirza-ghalib-ghazals')
soup = BS(response.content, "html.parser")
for child in soup.body.children:
   if child.name == 'script':
       child.decompose() 
print(soup.body.get_text())
