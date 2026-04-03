# app/services/csv_service.py

from app.services.search_service import search_company
from app.services.scrape_service import scrape_fast
from app.services.playwright_service import scrape_dynamic
from app.services.ai_service import extract_with_ai
from app.services.validator_service import validate_results

import pandas as pd
from io import StringIO
import json, re

async def process_csv(file):
    content = await file.read()
    df = pd.read_csv(StringIO(content.decode("utf-8")))
    companies = df.iloc[:, 0].tolist()

    results = []

    for company in companies:
        try:
            search = search_company(company)
            links = search.get("organic", [])

            extracted_data = []
            used_sources = []

            for item in links[:5]:
                link = item.get("link", "")

                if "linkedin.com" in link:
                    continue

                # 🔥 Step 1: fast scrape
                text = scrape_fast(link)

                # 🔥 Step 2: fallback
                if not text:
                    text = await scrape_dynamic(link)

                if not text:
                    continue

                ai_output = extract_with_ai(text, company)

                try:
                    parsed = json.loads(re.search(r"\{.*\}", ai_output, re.DOTALL).group())
                    extracted_data.append(parsed)
                    used_sources.append(link)
                except:
                    continue

                if len(extracted_data) >= 2:
                    break

            final = validate_results(extracted_data)

            results.append({
                "company": company,
                "CEO": final["CEO"],
                "Founded": final["Founded"],
                "Headquarters": final["Headquarters"],
                "source": ", ".join(used_sources)
            })

        except Exception as e:
            print("ERROR:", company, str(e))

            results.append({
                "company": company,
                "CEO": "Unknown",
                "Founded": "Unknown",
                "Headquarters": "Unknown",
                "source": ""
            })

    return {"data": results}