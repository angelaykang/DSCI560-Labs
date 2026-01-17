# DSCI 560 Lab Assignment 1

**Author**: Angela Kang  
**USC ID**: 8957777203  
**Date**: January 16, 2026

## Description

This lab sets up a Ubuntu Linux virtual machine, installs Python, and performs web scraping on CNBC World News.

## Requirements

- Python 3
- Selenium
- BeautifulSoup4

## Installation

```bash
sudo apt install python3-selenium python3-bs4
```

## Files

- `scripts/task_1.py` - Basic greeting script
- `scripts/web_scraper.py` - Scrapes CNBC website using Selenium
- `scripts/data_filter.py` - Parses HTML and creates CSV files
- `data/raw_data/web_data.html` - Raw HTML scraped from CNBC
- `data/processed_data/market_data.csv` - Market data output
- `data/processed_data/news_data.csv` - News data output

## Usage

```bash
# Run greeting script
python3 task_1.py

# Scrape CNBC website
python3 web_scraper.py

# Parse HTML and create CSV files
python3 data_filter.py
```