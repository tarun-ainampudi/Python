import requests
import time
import csv
import threading
from concurrent.futures import ThreadPoolExecutor

# Config
base_url = "https://www.results.manabadi.co.in/2023/AP/Inter/2nd-year/i2gen2023-ap.aspx"
start_htno = 2302230000
end_htno = 2302239999
max_retries = 3
max_workers = 10

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

# Locks for thread-safe file access
csv_lock = threading.Lock()
error_lock = threading.Lock()

# # Ensure CSV headers are written once
# with open("manabadi_results.csv", "w", newline='', encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow(["HTNO", "RawResultLine"])

def fetch_result(htno):
    for attempt in range(max_retries):
        try:
            url = f"{base_url}?htno={htno}&bustcache={int(time.time() * 1000)}"
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            # Look for line that starts with hall ticket number
            lines = response.text.split("\n")
            for line in lines:
                if f"{htno}|" in line:
                    write_to_csv(htno, line.strip())
                    return

            # If no valid line found
            if response.status_code == 200:
                continue
            else:
                log_error(htno, "No result line found")

        except Exception as e:
            if attempt == max_retries - 1:
                log_error(htno, f"Error: {str(e)}")
            time.sleep(1)

def write_to_csv(htno, result_line):
    global start_htno, end_htno
    with csv_lock:
        with open(f"manabadi_results_{start_htno}_{end_htno}.csv", "a", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([result_line])
        print(f"✅ Saved: {htno}")

def log_error(htno, message):
    with error_lock:
        with open("manabadi_errors.log", "a", encoding="utf-8") as f:
            f.write(f"{htno}: {message}\n")
        print(f"❌ Error: {htno} - {message}")

def main():
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(fetch_result, range(start_htno, end_htno + 1))

    print("\n🎯 All done. Results and errors written to disk safely.")

if __name__ == "__main__":
    main()
