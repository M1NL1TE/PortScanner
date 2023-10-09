import socket

# Dictionary that maps common port numbers to service names
port_to_service = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    1462: "world-lm",
    2179: "vmrdp",
}

def scan_ports(target_host, port_range):
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates socket object / 'AF_NET is for IPv4 and SOCK_STREAM is for a TCP socket
        sock.settimeout(1)  # Set a timeout of 1 second for the connection attempt
        result = sock.connect_ex((target_host, port))
        if result == 0:
            service = port_to_service.get(port, "Unknown")
            print(f"Port {port}/tcp is open - Service: {service}")
        sock.close()

if __name__ == "__main__":
    target_host = input("Enter the target host: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    
    port_range = (start_port, end_port)
    
    print(f"Scanning {target_host} for open ports in range {port_range[0]}-{port_range[1]}...")
    scan_ports(target_host, port_range)
