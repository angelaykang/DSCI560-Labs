"""
DSCI 560 - Lab Assignment 1
Author: Angela Kang
USC ID: 8957777203
Date: 01/16/2026
"""

import os
import csv
from bs4 import BeautifulSoup


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
raw_file = os.path.join(base_dir, "data", "raw_data", "web_data.html")
processed_dir = os.path.join(base_dir, "data", "processed_data")
os.makedirs(processed_dir, exist_ok=True)

# read html
with open(raw_file, "r", encoding="utf-8") as f:
    html_lines = f.readlines()

# parse html 
soup = BeautifulSoup("".join(html_lines), "html.parser")


print("Filtering fields")

# market data elements using CSS selectors
symbols = soup.select(".MarketCard-symbol")
positions = soup.select(".MarketCard-stockPosition")
changes = soup.select(".MarketCard-changesPct")

# write market data to csv
market_csv = os.path.join(processed_dir, "market_data.csv")
print("Storing Market data")
with open(market_csv, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["marketCard_symbol", "marketCard_stockPosition", "marketCard-changePct"])
    for s, p, c in zip(symbols, positions, changes):
        w.writerow([s.get_text(strip=True), p.get_text(strip=True), c.get_text(strip=True)])
print("CSV created: market_data.csv")

# extract news data elements
timestamps = soup.select(".LatestNews-timestamp")
news_csv = os.path.join(processed_dir, "news_data.csv")
print("Storing News data")
with open(news_csv, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["LatestNews-timestamp", "title", "link"])
    # process each timestamp and find associated article data
    for ts in timestamps:
        parent = ts.find_parent(["li", "div", "article"])
        a = parent.find("a", href=True) if parent else None
        title = a.get_text(strip=True) if a else ""
        link = a["href"] if a else ""
        # relative URLs to absolute URLs
        if link.startswith("/"):
            link = "https://www.cnbc.com" + link
        w.writerow([ts.get_text(strip=True), title, link])
print("CSV created: news_data.csv")
