import os
import sys
import requests
import re
from bs4 import BeautifulSoup

def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    # Check if the URL is from Medium
    if not re.match(r'https?://medium.com/', url):
        print('Please enter a valid Medium article URL.')
        sys.exit(1)

    # Send request to the URL
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

def collect_text(soup):
    text = f'URL: {url}\n\n'
    paragraphs = soup.find_all('p')
    for para in paragraphs:
        text += f"{para.text}\n\n"
    return text

def save_file(text):
    if not os.path.exists('./scraped_articles'):
        os.mkdir('./scraped_articles')
    filename = url.split("/")[-1]
    filename = re.sub(r'[^\w\s-]', '', filename)  # Remove special characters
    filename = re.sub(r'\s+', '_', filename)  # Replace whitespace with underscores
    filename = filename.strip('_')  # Remove leading/trailing underscores
    filepath = f'scraped_articles/{filename}.txt'

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(text)

    print(f'File saved as {filename}.txt in directory scraped_articles.')

if __name__ == '__main__':
    url = 'https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7'
    text = collect_text(get_page(url))
    save_file(text)