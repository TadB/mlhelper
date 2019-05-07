from bs4 import BeautifulSoup
import requests


def get_website_content(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    content = ''
    for post in soup.find_all(class_='post'):
        for p in post.find_all('p'):
            content += p.text
    return content

