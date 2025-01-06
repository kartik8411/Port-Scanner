#Port Scanner

a brief description of what this project does and who it's for

## Table of contents

- [Installation](#installation).
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

Instructions on how to install and set up the projects

##Features

- Scan a range of ports on a target host
 
- It uses multithreading to perform the scan concurrently for faster results.
 
- Outputs the open ports found within the specified range.
 
- Displays the total time taken to complete the scan.
 
    
##Usage

 Clone the repository
 
git clone https://github.com/yourusername/port-scanner.git

cd port-scanner

Run the script
python portscan.py

The script will prompt you to input:

   
   Host: The target IP address or hostname you want to scan.
   
   Starting port: The first port number to scan.
    
  Ending port: The last port number to scan.

##Example:-

Enter the host to scan (e.g., localhost or IP address): 127.0.0.1
Enter the starting port: 20
Enter the ending port: 80

 Output Example
Port 22 is OPEN
Port 80 is OPEN
Port scan completed in 0:00:01.234567
Open ports: [22, 80]

##How it Works

   - Input Validation: The script first checks the validity of the host and the port range.
   
   - Port Scanning: It scans the specified range of ports on the given host using multithreading for efficient performance.
   
   - Result Reporting: After the scan is completed, it lists the open ports found and shows the total time taken.

License

This project is licensed under the MIT License - see the LICENSE file for details.

    
