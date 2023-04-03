import requests
from bs4 import BeautifulSoup
import time

url = 'https://php.net'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')

for link in links:
    href = link.get('href')
    if href and 'http' not in href:
        page_url = url + href
        start_time = time.time()
        page_response = requests.get(page_url)
        end_time = time.time()
        page_load_time = end_time - start_time
        print(f'Page: {page_url}, Load time: {page_load_time:.2f} seconds')
