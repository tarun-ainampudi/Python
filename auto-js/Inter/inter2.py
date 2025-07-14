import requests
import time
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed

# Config
base_url = "https://www.results.manabadi.co.in/2023/AP/Inter/2nd-year/i2gen2023-ap.aspx"
start_htno = 2306230000
end_htno = 2306239999  # Increase this for large range
max_retries = 3
max_workers = 20  # Increase depending on your network capability

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

def fetch_result(htno):
    for attempt in range(max_retries):
        try:
            url = f"{base_url}?htno={htno}&bustcache={int(time.time() * 1000)}"
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            # Find and parse pipe-separated result line
            text = response.text
            parts = text.split("\n")
            for line in parts:
                if f"{htno}|" in line:
                    return htno, line.strip()

            return htno, "No result line found"
        except Exception as e:
            if attempt == max_retries - 1:
                return htno, f"Error: {str(e)}"
            time.sleep(1)  # Delay before retry

def main():
    all_results = []
    error_log = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(fetch_result, htno): htno for htno in range(start_htno, end_htno + 1)}

        for future in as_completed(futures):
            htno = futures[future]
            try:
                htno, result_line = future.result()
                if result_line.startswith("Error") or "No result" in result_line:
                    error_log.append((htno, result_line))
                else:
                    all_results.append((htno, result_line))
                    print(f"Fetched: {htno}")
            except Exception as e:
                error_log.append((htno, f"Exception: {e}"))

    # Write to CSV
    with open("manabadi_results.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["HTNO", "RawResultLine"])
        writer.writerows(all_results)

    # Write errors separately
    with open("manabadi_errors.log", "w", encoding="utf-8") as f:
        for htno, err in error_log:
            f.write(f"{htno}: {err}\n")

    print(f"\n✅ Completed. {len(all_results)} results fetched. {len(error_log)} errors logged.")

if __name__ == "__main__":
    main()
