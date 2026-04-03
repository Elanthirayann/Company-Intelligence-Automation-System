# app/services/scrapy_service.py

import requests
from bs4 import BeautifulSoup

def scrape_fast(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=8)

        if res.status_code != 200:
            return ""

        soup = BeautifulSoup(res.text, "html.parser")

        for tag in soup(["script", "style"]):
            tag.extract()

        text = soup.get_text(" ", strip=True)

        return text[:4000] if len(text) > 300 else ""

    except:
        return ""