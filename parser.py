import requests
from bs4 import BeautifulSoup

# requesting the content of webpage
r = requests.get("https://www.rekhta.org/collections/dil-men-ab-yuun-tire-bhuule-hue-gam-aate-hain-faiz-ahmad-faiz-ghazals")

#now parsing the html in an object named soup
soup = BeautifulSoup(r.text, 'html.parser')

#After analyzing the tags layout of desired content, specifically extracting the tags containing poetry
results = soup.find_all('div', attrs={'class':'c'})

#Now looping through the found tags to print the poetry

for result in results[0:9]:
    line_one = result.contents[0].text
    line_two = result.contents[1].text
    print(line_one)
    print(line_two)
    print("\n")
