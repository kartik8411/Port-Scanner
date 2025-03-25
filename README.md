# Port Scanner

### Port Scanner is a Python-based tool that allows users to scan a range of ports on a specified host to identify which ports are open. The script uses multithreading to speed up the scanning process, making it more efficient for larger port ranges. After completing the scan, it displays the open ports along with the time taken for the scan, helping network administrators, security professionals, and developers quickly assess the status of networked systems. This tool is useful for anyone needing a lightweight and fast solution for port scanning tasks.

## Table of contents

- ### [Installation](#installation).
- ### [Usage](#usage)
- ### [Contributing](#contributing)
- ### [License](#license)

## Installation

 ### 1.  Clone the repository
  ```
     git clone https://github.com/kartik8411/Port-Scanner.git
   ```
   
### 2.   Go to the project directory
   ```
    cd portscanner
   ```

### 3.  Run the script 
  ```
  python portscanner.py
  ```

## Features

- ### Scan a range of ports on a target host
 
- ### It uses multithreading to perform the scan concurrently for faster results.
 
- ### Outputs the open ports found within the specified range.
 
- ### Displays the total time taken to complete the scan.
 
    
## Usage

### The script will prompt you to input:

   
###  - ```Host```:  The target IP address or hostname you want to scan.
   
###  - ```Starting port```: The first port number to scan.
    
###  - ```Ending port```:  The last port number to scan.

    

## Example:-

- Enter the host to scan (e.g., localhost or IP address): 127.0.0.1

- Enter the starting port: 20

- Enter the ending port: 80

## Output Example:-

- Port 22 is OPEN

- Port 80 is OPEN

- Port scan completed in 0:00:01.234567

- Total Open ports: [22, 80]

## How it Works

   - Input Validation: The script first checks the validity of the host and the port range.
   
   - Port Scanning: It scans the specified range of ports on the given host using multithreading for efficient performance.
   
   - Result Reporting: After the scan is completed, it lists the open ports found and shows the total time taken.

License

This project is licensed under the MIT License - see the LICENSE file for details.

    
