import os
import xml.etree.ElementTree as ET
import json
import re
import requests
from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# CLOUDFLARE CONFIGURATION
CLOUDFLARE_WORKER_URL = "https://sensei-blog-api.wico-dev.workers.dev"


def get_latest_engineering_trend():
    """Fetches the top trend from Google News RSS without requiring an API key."""
    search_keywords = '"structural engineering" OR "megastructures" OR "civil engineering technology"'
    rss_url = f"https://news.google.com/rss/search?q={requests.utils.quote(search_keywords)}&hl=en-US&gl=US&ceid=US:en"

    try:
        response = requests.get(rss_url, timeout=15)
        response.raise_for_status()
        root = ET.fromstring(response.content)

        item = root.find(".//item")
        if item is not None:
            return {
                "title": item.find("title").text,
                "link": item.find("link").text,
                "pubDate": item.find("pubDate").text
            }
    except Exception as e:
        print(f"[-] Failed to query news trend pipeline: {e}")
    return None


def generate_sensei_insight(trend_data):
    """Uses LangChain and Google Gemini to synthesize raw news into the brand persona."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("[-] Halting: GOOGLE_API_KEY environment variable is not set.")
        return None

    # Initialize the Gemini engine via LangChain
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.7,
        google_api_key=api_key
    )

    system_prompt = (
        "You are Structural Sensei (@StructuralSensei), an elite technical manager, civil engineering professional, "
        "and disciplined Karateka. Your mission is to bridge technical engineering theory with deep martial arts philosophy.\n\n"
        "Your tone must be authoritative, highly analytical, clear, concise, and deeply grounded in discipline. Avoid generic corporate fluff.\n\n"
        "You must output exactly a JSON object containing the following keys:\n"
        "- 'blogTitle': A striking, unique title blending the engineering topic with a martial arts conceptual framework.\n"
        "- 'modernTrend': A breakdown of the current engineering event or breakthrough provided in the news context.\n"
        "- 'technicalHistory': The deeper scientific, materials science, or structural history behind this phenomenon.\n"
        "- 'karatekaVector': The Sensei Insight—how this specific engineering problem maps directly onto traditional Karate principles, balance, stances, mechanics, or discipline."
    )

    human_prompt = (
        "Analyze this current industry trend:\n"
        "Raw Title: {trend_title}\n"
        "Source Link: {trend_link}\n"
        "Published Date: {trend_date}\n\n"
        "Generate a highly specific, unique weekly article matching your structural rules. "
        "Ensure your output is valid, raw JSON only. Do not wrap it in markdown code blocks like ```json."
    )

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", human_prompt)
    ])

    chain = prompt_template | llm

    try:
        execution_input = {
            "trend_title": trend_data["title"],
            "trend_link": trend_data["link"],
            "trend_date": trend_data["pubDate"]
        }
        response = chain.invoke(execution_input)

        clean_content = response.content.strip()
        if clean_content.startswith("```json"):
            clean_content = clean_content.replace("```json", "").replace("```", "").strip()

        return json.loads(clean_content)
    except Exception as e:
        print(f"[-] Gemini generation or parsing anomaly: {e}")
        return None


def main():
    print("[+] Initializing weekly Dojo content automation engine via Gemini...")
    trend = get_latest_engineering_trend()

    if not trend:
        print("[-] No active trend parsed. Exiting pipeline loop.")
        return

    print(f"[+] Target trend identified: {trend['title']}")
    blog_payload = generate_sensei_insight(trend)

    if not blog_payload:
        print("[-] Generation failed. Exiting pipeline loop.")
        return

    raw_title = blog_payload["blogTitle"]
    slug = raw_title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s-]+', '-', slug).strip('-')

    worker_payload = {
        "slug": slug,
        "title": blog_payload["blogTitle"],
        "trend": blog_payload["modernTrend"],
        "history": blog_payload["technicalHistory"],
        "vector": blog_payload["karatekaVector"],
        "published_date": datetime.now().strftime("%Y-%m-%d")
    }

    print(f"[+] Transmitting generated lesson '{raw_title}' to Cloudflare edge network...")
    try:
        response = requests.post(CLOUDFLARE_WORKER_URL, json=worker_payload, timeout=15)
        if response.status_code == 200 or response.status_code == 201:
            print(f"[+] Execution complete. Post live at D1 database storage via slug: {slug}")
        else:
            print(f"[-] Cloudflare API rejected package. Status: {response.status_code}")
    except Exception as e:
        print(f"[-] Direct connection to Cloudflare worker broke down: {e}")


if __name__ == "__main__":
    main()