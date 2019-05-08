import os

from bs4 import BeautifulSoup
import requests
from urllib.request import urlretrieve
from datetime import datetime


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
    # add time stamp to avoid image path collision
    t_stamp = datetime.utcnow().strftime('%y%m%d%H%M%S')
    folder = 'images/'
    filename = folder+t_stamp+url.split('/')[-1]
    basedir = os.path.abspath(os.path.dirname(__file__))
    # saving image
    img = requests.get(url)
    with open(os.path.join(basedir, filename), 'wb') as f:
        f.write(img.content)
    return filename
