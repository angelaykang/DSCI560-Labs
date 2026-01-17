"""
DSCI 560 - Lab Assignment 1
Author: Angela Kang
USC ID: 8957777203
Date: 01/16/2026
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

url = "https://www.cnbc.com/world/?region=world"

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
raw_dir = os.path.join(base_dir, "data", "raw_data")
os.makedirs(raw_dir, exist_ok=True)

out_path = os.path.join(raw_dir, "web_data.html")

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)

time.sleep(5)

html_content = driver.page_source

with open(out_path, "w", encoding="utf-8") as f:
	f.write(html_content)

driver.quit()

print("Saved web_data.html")
