# 🌐 Amazon Product Scraper

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A robust Python web scraper that extracts product data from Amazon, perfect for price tracking, market research, and competitive analysis.

## ✨ Features
- **Product Data Extraction**: Scrapes titles, prices, and URLs
- **CSV Export**: Saves data in structured format for analysis
- **Anti-Bot Bypass**: Uses rotating headers to avoid detection
- **Error Handling**: Gracefully manages missing elements and connection issues
  
## 📋Usage
- Enter an Amazon product URL when prompted (e.g., https://www.amazon.com/dp/B08N5KWB9H).
- Check the generated amazon_products.csv for results.

## ⚠️ Legal Note
- This is for educational purposes only.
- Respect Amazon's robots.txt and scraping policies.
- Add delays (time.sleep()) to avoid overwhelming servers.

## 🛠️ Installation
```bash
# Clone the repository
git clone https://github.com/siddhanth36/-Web-Scraper.git
cd -Web-Scraper

# Install dependencies
pip install -r requirements.txt

#  Usage
python3 web_scraper.py
