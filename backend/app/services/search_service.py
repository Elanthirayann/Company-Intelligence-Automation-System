# app/services/search_service.py

import requests, os
from dotenv import load_dotenv

load_dotenv()

API = os.getenv("SERPER_API_KEY")

def search_company(company):
    return requests.post(
        "https://google.serper.dev/search",
        json={"q": f"{company} CEO founder headquarters", "num": 5},
        headers={"X-API-KEY": API}
    ).json()