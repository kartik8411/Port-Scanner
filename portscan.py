import socket
import pyfiglet
from threading import Thread
from colorama import Fore
from datetime import datetime  # Import datetime module

banner = pyfiglet.figlet_format('Port  Scanner', font='doom')
print(Fore.BLUE + banner)

# Function to scan a single port
def scan_port(host, port, open_ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set timeout for the connection attempt
    result = sock.connect_ex((host, port))  # Try connecting to the target port
    if result == 0:  # Connection successful
        print(f"Port {port} is OPEN")
        open_ports.append(port)  # Add to open ports list
    sock.close()

# Function to perform the port scan with threading
def scan_ports(host, start_port, end_port):
    threads = []
    open_ports = []  # List to keep track of open ports
    for port in range(start_port, end_port + 1):
        t = Thread(target=scan_port, args=(host, port, open_ports))
        threads.append(t)
        t.start()

    # Join all threads (wait for all to finish)
    for t in threads:
        t.join()

    return open_ports  # Return the list of open ports

# Example usage
host = input('Enter the host to scan (e.g., localhost or IP address): ')  # IP address of the target machine (localhost in this case)

# Validate the host
try:
    socket.gethostbyname(host)
except socket.gaierror:
    print(Fore.BLACK + f"Invalid host: {host}")
    exit()

# Get the port range from the user
try:
    start_port = int(input('Enter the starting port: '))
    end_port = int(input('Enter the ending port: '))
except ValueError:
    print(Fore.RED + "Invalid input. Please enter numeric values for ports.")
    exit()

# Validate port range
if start_port < 1 or end_port > 65535 or start_port > end_port:
    print(Fore.RED + "Please enter valid port range (1-65535) where the start port is less than or equal to the end port.")
    exit()

# Record the start time
start_time = datetime.now()

# Start the port scan and get the open ports
open_ports = scan_ports(host, start_port, end_port)

# Record the end time
end_time = datetime.now()

# Calculate the total time taken
elapsed_time = end_time - start_time
print(f"Port scan completed in {elapsed_time}")

# Print only the open ports
if open_ports:
    print(f"Open ports: {open_ports}")
else:
    print("No open ports found.")
