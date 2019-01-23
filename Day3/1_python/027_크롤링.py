#pip3 install requests
#pip3 install beautifulsoup4

import requests
from bs4 import BeautifulSoup

response = requests.get('https://ridibooks.com/category/bestsellers/2200')
response.encoding = 'utf-8'
html = response.text
#print(html)

soup = BeautifulSoup(html, 'html.parser')
#for tag in soup.select('#course_list > .course > a'):
#    print(tag.text, tag['href'])

title = soup.select('.title_text')
print(title)

for i, j in enumerate(title, 1):
    print(i, j.text.strip())