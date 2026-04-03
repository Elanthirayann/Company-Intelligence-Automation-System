# app/services/ai_service.py

import os, json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_with_ai(text, company):
    try:
        prompt = f"""
Extract company info for: {company}

Return JSON:
{{
  "CEO": "...",
  "Founded": "...",
  "Headquarters": "..."
}}

Rules:
- If missing → "Unknown"
- No guessing

TEXT:
{text[:3000]}
"""

        res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )

        return res.choices[0].message.content.strip()

    except:
        return json.dumps({
            "CEO": "Unknown",
            "Founded": "Unknown",
            "Headquarters": "Unknown"
        })