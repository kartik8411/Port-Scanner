![logo](https://github.com/kartik8411/Port-Scanner/blob/main/image1.png)
# Port Scanner

### Port Scanner is a Python-based tool that allows users to scan a range of ports on a specified host to identify which ports are open. The script uses multithreading to speed up the scanning process, making it more efficient for larger port ranges. After completing the scan, it displays the open ports along with the time taken for the scan, helping network administrators, security professionals, and developers quickly assess the status of networked systems. This tool is useful for anyone needing a lightweight and fast solution for port scanning tasks.

## Installation

 ### 1.  Clone the repository
  ```
     git clone https://github.com/kartik8411/Port-Scanner.git
   ```
   
### 2.   Go to the project directory
   ```
    cd portscan.py
   ```

### 3.  Run the script 
  ```
  python portscan.py
  ```


## Requirements
### - `Python 3`
### - `pyfiglet` - for generating the ASCII banner.
### - `colorama` - for coloring the output in the terminal.

### You can install the required dependencies using pip:
```
pip install pyfiglet colorama
```

## Technologies Used:
1. ### Python 3
2. ### socket for network communication
3. ### pyfiglet to create ASCII banners
4. ### colorama for adding colors to the terminal output
5. ### threading for parallel processing
   
## Features
- ### Scans a specified range of ports on a given host.
- ### Multi-threading support for faster scanning.
- ### Displays open ports along with a visual banner and status updates.
- ### Displays the total time taken to complete the scan.
- ### Handles invalid inputs for host and port range gracefully.

## Usage

  ### 1. Clone or download this repository to your local machine.

  ### 2. Open a terminal or command prompt and navigate to the directory where the script is located.

  ### 3. Run the script:
  ```
python portscan.py
```

### 4. The script will prompt you to input:

   
###  - ```Host```: The host you want to scan  (e.g., localhost or IP address like 192.168.1.1).
   
###  - ```Starting port```: The first port number to scan.
    
###  - ```Ending port```:  The last port number to scan.

    
![logo](https://github.com/kartik8411/Port-Scanner/blob/main/image2.png)

## How it Works

   ### - ```Input Validation```: The script first checks the validity of the host and the port range.
   
   ### - ```Port Scanning```: It scans the specified range of ports on the given host using multithreading for efficient performance.
   
   ### - ```Result Reporting```: After the scan is completed, it lists the open ports found and shows the total time taken.

# License

### This project is licensed under the MIT License - see the LICENSE file for details.

    
