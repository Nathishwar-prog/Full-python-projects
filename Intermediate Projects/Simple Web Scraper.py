# scraper.py
import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

def scrape_quotes(base_url, pages_to_scrape=1):
    quotes = []
    
    for page_num in range(1, pages_to_scrape + 1):
        url = f"{base_url}/page/{page_num}/"
        print(f"Scraping {url}...")
        
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch page {page_num}")
            continue
            
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for quote_div in soup.find_all('div', class_='quote'):
            text = quote_div.find('span', class_='text').get_text(strip=True)
            author = quote_div.find('small', class_='author').get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in quote_div.find_all('a', class_='tag')]
            
            quotes.append({
                'text': text,
                'author': author,
                'tags': ', '.join(tags)
            })
    
    return quotes

def save_to_csv(quotes, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['text', 'author', 'tags']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for quote in quotes:
            writer.writerow(quote)
    
    print(f"Saved {len(quotes)} quotes to {filename}")

if __name__ == '__main__':
    BASE_URL = "http://quotes.toscrape.com"
    pages = 3  # Number of pages to scrape
    
    quotes_data = scrape_quotes(BASE_URL, pages)
    save_to_csv(quotes_data, 'quotes.csv')
    
    # Display some sample data
    print("\nSample quotes:")
    for i, quote in enumerate(quotes_data[:3], 1):
        print(f"\nQuote {i}:")
        print(f"Text: {quote['text']}")
        print(f"Author: {quote['author']}")
        print(f"Tags: {quote['tags']}")
