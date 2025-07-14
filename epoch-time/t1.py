import time
from datetime import datetime, timezone, timedelta

# Target timestamp
target_timestamp = 1748187046000//1000

while True:
    now_utc = datetime.now(timezone.utc)
    target_utc = datetime.fromtimestamp(target_timestamp, tz=timezone.utc)

    remaining = target_utc - now_utc
    if remaining.total_seconds() <= 0:
        print("\n⏰ Timer reached!")
        break

    # Format remaining time
    hours, remainder = divmod(int(remaining.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"\r⏳ Time remaining: {hours:02d}:{minutes:02d}:{seconds:02d}", end="")
    time.sleep(1)
