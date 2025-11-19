import asyncio
import aiohttp
from bs4 import BeautifulSoup
import json
import pandas as pd
from tqdm import tqdm

# Extract links from one HTML document
def get_links(html):
    soup = BeautifulSoup(html, "html.parser")
    main = soup.find(id="main")
    if not main:
        return []

    links = []
    for a in main.find_all("a", href=True):
        if (a.get("class") in [None, []] and 
            not a.get("title") and 
            a.get("rel") == ["bookmark"] and 
            not a.findChildren()):
            links.append({
                "href": a["href"],
                "text": a.get_text(strip=True)
            })
    return links


# Fetch a single page
async def fetch_page(session, url):
    try:
        async with session.get(url, timeout=20) as resp:
            if resp.status == 200:
                html = await resp.text()
                return html
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return None


# Worker function to fetch and extract
async def process_page(session, page_num):
    url = f"https://naasongs.com.co/page/{page_num}"
    html = await fetch_page(session, url)
    if not html:
        return {"page": page_num, "links": []}
    links = get_links(html)
    return {"page": page_num, "links": links}


# Main async runner
async def main():
    pages = range(1, 465)
    results = []

    connector = aiohttp.TCPConnector(limit=20)  # 20 concurrent connections
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [process_page(session, i) for i in pages]
        for future in tqdm(asyncio.as_completed(tasks), total=len(tasks)):
            result = await future
            results.append(result)
    print(len(results), "pages processed.")
    # Save as JSON
    with open("naasongs_links.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    asyncio.run(main())
