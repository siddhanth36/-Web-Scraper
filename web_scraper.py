#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import csv

def scrape_amazon_product(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")  # Use lxml for speed

        # Extract title (fallback to alternative selectors)
        title = soup.find("span", id="productTitle")
        if not title:
            title = soup.find("h1", class_="a-size-large")
        title = title.get_text(strip=True) if title else "Title not found"

        # Extract price (handles multiple formats)
        price_span = soup.find("span", class_="a-price")
        if price_span:
            price = price_span.find("span", class_="a-offscreen").get_text(strip=True)
        else:
            price = "Price not found"

        print(f"📦 Title: {title}")
        print(f"💰 Price: {price}")

        # Save to CSV
        with open("amazon_products.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([title, price, url])
        print("✅ Data saved to 'amazon_products.csv'")

    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    print("🕷️ Amazon Product Scraper")
    url = input("Enter Amazon product URL: ").strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url  # Auto-add protocol if missing
    scrape_amazon_product(url)
