"""
Webscraper
@author: OG
"""
import urllib3
from bs4 import BeautifulSoup
def despacito():
    http = urllib3.PoolManager()
    url = 'https://www.youtube.com/watch?v=kJQP7kiw5Fk'
    page = http.request('GET', url)
    soup = BeautifulSoup(page.data, 'html.parser') 
    name_box = soup.find('div', attrs={'class':'watch-view-count'})
    views = name_box.text.strip()
    return views

def world_population():
    # currently not working
    http = urllib3.PoolManager()
    url = 'https://www.google.com/search?q=current+human+population'
    page = http.request('GET', url)
    soup = BeautifulSoup(page.data, 'html.parser')
    print(soup)
    box = soup.find('div', attrs={'class':'Z0LcW'})
    population = box.text.strip()
    return population

if __name__ == '__main__':
    print(despacito())