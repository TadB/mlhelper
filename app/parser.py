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


def get_images(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    for post in soup.find_all(class_='post'):
        for img in post.find_all('img'):
            yield img['src']


def save_image(url):
    pass
