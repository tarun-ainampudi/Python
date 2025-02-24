import socket

def check_port(host, port,timeout=5):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except:
        return False
    
print("processing.......")
for i in range(65536):
    host = "172.18.10.10"
    port = i
    if check_port(host, port):
        print(f"Port {port} on {host} is accessible")