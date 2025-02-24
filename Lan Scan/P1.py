import threading
from scapy.all import ARP, Ether, srp
from concurrent.futures import ThreadPoolExecutor

# Define the network range based on IP and Subnet Mask
network_range = "172.19.128.0/21"

# Function to scan a specific IP
def scan_ip(ip):
    # Create ARP request
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request

    # Send the packet and get response
    result = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    # Parse the result and return available devices
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices

# Function to scan network range with multiple threads
def scan_network(network_range):
    ip_list = [f"172.19.{i}.{j}" for i in range(128, 136) for j in range(0, 256)]  # 172.19.128.0/21 range

    # Create a thread pool for scanning
    devices_found = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = list(executor.map(scan_ip, ip_list))
    
    # Collect all the found devices from the threads
    for result in results:
        if result:
            devices_found.extend(result)
    
    return devices_found

if __name__ == "__main__":
    print(f"Scanning network {network_range}...")
    devices = scan_network(network_range)

    # Print found devices
    if devices:
        print("Devices found in the network:")
        for device in devices:
            print(f"IP: {device['ip']}, MAC: {device['mac']}")
    else:
        print("No devices found.")
