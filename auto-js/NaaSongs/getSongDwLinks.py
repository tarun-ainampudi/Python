import json
import requests
from bs4 import BeautifulSoup
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "https://naasongs.com.co"

# Disable SSL warnings (optional)
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def extract_links_from_html(html):
    soup = BeautifulSoup(html, "html.parser")

    doc = soup.find(class_="entry-content clearfix")
    if not doc:
        return {}

    paragraphs = doc.find_all("p")
    links_data = {}

    for p in paragraphs:
        anchors = p.find_all("a", href=True)
        if not anchors:
            continue

        lines = [line.strip() for line in p.get_text("\n").split("\n") if line.strip()]
        title = lines[0] if lines else "Untitled"
        links_data[title] = {}

        for j, a in enumerate(anchors):
            index = lines[j + 1] if len(lines) > j + 1 else a.get_text(strip=True) or "No Index"
            links_data[title][index] = a["href"]

    return links_data


def getMovieObj(url):
    try:
        # Handle both absolute and relative URLs
        full_url = url if url.startswith("http") else f"{BASE_URL.rstrip('/')}/{url.lstrip('/')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(full_url, timeout=15, verify=False, headers=headers)

        if res.status_code != 200:
            print(f"⚠️ Failed to fetch {full_url}: {res.status_code}")
            return {}

        return extract_links_from_html(res.text)
    except Exception as e:
        print(f"❌ Error fetching {url}: {e}")
        return {}


# === MAIN ===
with open('naasongs_links.json', "r", encoding="utf-8") as f:
    data = json.load(f)

newData = {}

# Prepare tasks
tasks = {}
for page in data:
    for link in page['links']:
        text = link['text'].strip()
        href = link['href'].strip()
        if (
            href
            and text
            and not re.search(r"song", text.lower(), re.IGNORECASE)
            and text not in newData
        ):
            tasks[text] = href

print(f"🚀 Fetching {len(tasks)} movie pages in parallel...")

# Parallel fetching
MAX_THREADS = 20
with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
    future_to_text = {executor.submit(getMovieObj, href): text for text, href in tasks.items()}

    for future in as_completed(future_to_text):
        text = future_to_text[future]
        try:
            result = future.result()
            if result:
                newData[text] = result
                print(f"✅ {text} (got {len(result)} items)")
            else:
                print(f"⚠️ {text} returned empty object")
        except Exception as e:
            print(f"❌ {text}: {e}")

# Save output
with open("naasongs_dwlinks.json", "w", encoding="utf-8") as f:
    json.dump(newData, f, ensure_ascii=False, indent=4)

print("🎉 Done! Results saved to naasongs_dwlinks.json")
