# Scrape Flipkart Product Reviews and Save to CSV
# Requirements: requests, beautifulsoup4, pandas
# Usage: Run this script in your project directory

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Change this to the URL of a Flipkart product with many reviews
PRODUCT_URL = "https://www.flipkart.com/search?q=mobile"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}


def get_review_links(product_url, max_products=5):
    """Get product page links from a search result page."""
    res = requests.get(product_url, headers=HEADERS)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = []
    for a in soup.select('a._1fQZEK'):
        href = a.get('href')
        if href:
            links.append('https://www.flipkart.com' + href)
        if len(links) >= max_products:
            break
    return links


def get_reviews_from_product(product_page_url, max_reviews=30):
    """Scrape reviews from a single product page."""
    reviews = []
    page = 1
    while len(reviews) < max_reviews:
        url = product_page_url + f"&page={page}"
        res = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(res.text, 'html.parser')
        review_blocks = soup.select('div._16PBlm')
        if not review_blocks:
            break
        for block in review_blocks:
            review = block.select_one('div.t-ZTKy div')
            if review:
                text = review.get_text(strip=True)
                reviews.append(text)
            if len(reviews) >= max_reviews:
                break
        page += 1
        time.sleep(1)  # Be polite to the server
    return reviews


def main():
    product_links = get_review_links(PRODUCT_URL, max_products=5)
    all_reviews = []
    for link in product_links:
        reviews = get_reviews_from_product(link, max_reviews=30)
        for r in reviews:
            all_reviews.append({'review_text': r})
        print(f"Scraped {len(reviews)} reviews from {link}")
        time.sleep(2)
    print(f"Total reviews scraped: {len(all_reviews)}")
    df = pd.DataFrame(all_reviews)
    df.to_csv('reviews.csv', index=False)
    print("Saved to reviews.csv")

if __name__ == "__main__":
    main()
