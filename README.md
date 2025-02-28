# Port Scanner Script

This Python script performs a simple port scan on a given IP address within a specified port range.

## Features

-   **IP and Port Range Input:** Takes user input for the target IP address and the range of ports to scan.
-   **Port Discovery:** Scans the specified ports and identifies open ports.
-   **Progress Bar:** Provides a visual progress bar during the scan's completion.
-   **ASCII Art:** Displays a fancy ASCII art header.

## Prerequisites

-   Python 3.x
-   No external libraries are required (uses the built-in `socket`, `os`, `sys`, and `time` modules).

## How to Use

1.  **Save the script:** Save the Python code as a `.py` file (e.g., `port_scanner.py`).
2.  **Run the script:** Open a terminal or command prompt and run the script using the following command:

    ```bash
    python port_scanner.py
    ```

3.  **Enter the input:** The script will prompt you to enter the following:
    -      The target IP address.
    -      The starting port number.
    -      The ending port number.
4.  **View the results:** The script will display the scan results, showing which ports are open. A progress bar will appear at the end.

## Code Explanation

-   **ASCII Art:** The script starts by printing ASCII art for visual appeal.
-   **User Input:** The script prompts the user to enter the target IP address and the port range.
-   **`port_discovery(ip_input, port_start, port_end)` function:**
    -      Iterates through the specified port range.
    -      Creates a socket object for each port.
    -      Attempts to connect to the target IP and port.
    -      Prints a message if the port is open.
    -      Closes the socket.
-   **`progress_bar(duration=5, length=30)` function:**
    -   Displays a progress bar with a percentage completed.
    -   Uses sys.stdout.write and flush to keep the progress bar on one line.
    -   Uses time.sleep to control the speed of the progress bar.
-   **Main execution:** Calls the `port_discovery` function with the user-provided input.

## Example
Enter the IP address: 127.0.0.1
Enter the port number: 80
Enter An End port: 85
[+] scaning the target 127.0.0.1
[✔] port 80 is open
scan was completed
[##############################] 100%
[✔] Completed!
