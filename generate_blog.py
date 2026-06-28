import os
import re
import json
import requests
from datetime import datetime, timezone
from pathlib import Path
from google import genai

API_ENDPOINT = "https://sensei-blog-api.wico-pydev.workers.dev/api/posts"
KEY_PATH = Path(__file__).parent / "assets" / "api_key.txt"

if os.environ.get("GOOGLE_API_KEY"):
    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
elif KEY_PATH.exists():
    GOOGLE_API_KEY = KEY_PATH.read_text().strip()
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
else:
    print("[-] Halting: GOOGLE_API_KEY environment variable or assets/api_key.txt not found.")
    print("[-] Generation failed. Exiting pipeline loop.")
    exit(0)

print("[+] Initializing weekly Dojo content automation engine via Gemini...")
client = genai.Client(api_key=GOOGLE_API_KEY)


def fetch_industry_trend():
    # Ask Gemini to browse or identify the latest structural engineering trends
    # using a very simple prompt before the main synthesis
    discovery_prompt = "Identify the most significant, current news topic or trend in Structural Engineering for this week. Return ONLY the trend name and context in one sentence."

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=discovery_prompt
    )
    trend = response.text.strip()
    print(f"[+] Dynamically discovered trend: {trend}")
    return trend


def generate_slug(title):
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s-]+', '-', slug).strip('-')
    return slug


def run_pipeline():
    try:
        current_trend = fetch_industry_trend()

        prompt = f"""
        You are Structural Sensei, an expert engineering technical manager and efficiency architect.
        Analyze this current market or technical trend: "{current_trend}"

        Synthesize a brilliant, high-value educational directive for professional engineers.
        You MUST respond strictly with raw, valid JSON matching the exact schema definition below. 
        Do not wrap your output in markdown formatting blocks, just return the raw text object.

        Required JSON Layout Structure:
        {{
            "title": "A powerful, definitive title blending structural engineering concepts with automation/career strategy.",
            "history": "Deep technical analysis or historical background context explaining the core engineering concepts behind this trend.",
            "vector": "An actionable, advanced system analysis breakdown, complete with practical implementation logic, python optimization strategies, or geometric formula considerations to automate or solve this challenge."
        }}
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        response_text = response.text.strip()

        # UI-Safe Markdown Stripping: Bypasses the chat renderer bug
        bt = "`" * 3
        if response_text.startswith(bt):
            response_text = response_text.replace(bt + "json", "").replace(bt, "").strip()

        payload_data = json.loads(response_text)

        title = payload_data.get("title", "Untitled Mastery Document")
        slug = generate_slug(title)
        published_date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

        final_payload = {
            "slug": slug,
            "title": title,
            "trend": current_trend,
            "history": payload_data.get("history", ""),
            "vector": payload_data.get("vector", ""),
            "published_date": published_date
        }

        print(f"[+] Transmitting generated lesson '{title}' to Cloudflare edge network...")

        headers = {"Content-Type": "application/json"}
        cf_response = requests.post(API_ENDPOINT, json=final_payload, headers=headers)

        if cf_response.status_code == 201:
            print(f"[+] Execution complete. Post live at D1 database storage via slug: {slug}")
        else:
            print(f"[-] Cloudflare edge transmission error (Status: {cf_response.status_code}): {cf_response.text}")
            print("[-] Halting pipeline loops.")

    except json.JSONDecodeError:
        print("[-] System Error: Failed to parse clean structural JSON from Gemini engine.")
        print(f"[-] Raw capture dump: {response_text}")
    except Exception as e:
        print(f"[-] Critical Pipeline Exception: {str(e)}")
        print("[-] Exiting runtime loop.")


if __name__ == "__main__":
    run_pipeline()