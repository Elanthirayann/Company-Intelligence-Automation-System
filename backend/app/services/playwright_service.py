# app/services/playwright_service.py

from playwright.sync_api import sync_playwright
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor()

def _scrape_sync(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto(url, timeout=15000)
            page.wait_for_timeout(2000)

            content = page.inner_text("body")

            browser.close()

            return content[:4000] if len(content) > 300 else ""

    except Exception as e:
        print("PLAYWRIGHT ERROR:", str(e))
        return ""


# ✅ THIS IS THE IMPORTANT PART
async def scrape_dynamic(url):
    import asyncio
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, _scrape_sync, url)