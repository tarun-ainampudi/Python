import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

base_url = "https://www.results.manabadi.co.in/2023/AP/Inter/2nd-year/i2gen2023-ap.aspx"
start_htno = 2306237000
end_htno = 2306237999

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "referer": "https://www.results.manabadi.co.in/2023/AP/Inter/2nd-year/AP-Intermediate-2nd-year-regular-exam-results-Apr-2023-.htm"
}

results = {}

def fetch_result(htno):
    url = f"{base_url}?htno={htno}&bustcache={int(time.time() * 1000)}"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return htno, response.text
    except Exception as e:
        return htno, f"Error: {str(e)}"

def main():
    with ThreadPoolExecutor(max_workers=100) as executor:
        future_to_htno = {executor.submit(fetch_result, htno): htno for htno in range(start_htno, end_htno + 1)}

        with open("manabadi_results.txt", "w", encoding="utf-8") as file:
            for future in as_completed(future_to_htno):
                htno = future_to_htno[future]
                try:
                    htno, content = future.result()
                    print(f"Fetched result for {htno}")
                    file.write(f"\n----- Result for HTNO: {htno} -----\n{content}\n")
                except Exception as exc:
                    print(f"HTNO {htno} generated an exception: {exc}")

if __name__ == "__main__":
    main()
