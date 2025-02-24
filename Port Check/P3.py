import socket
from concurrent.futures import ThreadPoolExecutor
import webbrowser

def check_port(host, port, timeout=5):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except:
        return False

def scan_port(host, port):
    if check_port(host, port):
        url=f"http://{host}:{port}/login?"
        print(f"http://{host}:{port} is accessible")
        webbrowser.open(url)

if __name__ == "__main__":
    host = "172.18.10.10"
    max_workers = 100000  # Number of threads to be used; adjust based on your CPU capabilities
    print("Processing...")

    # Use ThreadPoolExecutor for concurrent port scanning
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(lambda port: scan_port(host, port), range(65536))

    print("Completed.")

