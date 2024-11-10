import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com'

def get_all_pages(url):
    page_urls = []
    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        page_urls.append(url)
        next_button = soup.find('li', class_='next')
        if next_button:
            next_page_url = next_button.find('a')['href']
            url = 'http://books.toscrape.com/catalogue/' + next_page_url
        else:
            break
    return page_urls

def get_books_from_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    book_titles = [a['title'] for a in soup.select('h3 a')]
    return book_titles

all_pages = get_all_pages(url)

all_book_titles = []
for page in all_pages:
    all_book_titles.extend(get_books_from_page(page))

for title in all_book_titles:
    print(title)
