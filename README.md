# Python Download Simulator

This Python script simulates a file download with a user-defined download speed and file size. It provides a simple command-line interface to set the download speed and then simulate downloading a file, showing a progress update in the terminal.

## Features

* **Set Download Speed:** Allows the user to specify the simulated download speed in various units: Bps, Kbps, Mbps, Gbps, Tbps, Pbps.
* **Simulate Download:** Enables the user to enter the size of a file (in MB) to download and simulates the download process based on the set speed, with slight random fluctuations for realism.
* **Progress Display:** Shows a dynamic progress update in the terminal during the simulated download, indicating the amount downloaded and the percentage complete.
* **Estimated Time:** Displays the total time taken for the simulated download to complete.

## How to Use

1.  **Save the script:** Save the Python code (provided in the previous response) as a `.py` file (e.g., `download_simulator.py`).

2.  **Open a terminal or command prompt:** Navigate to the directory where you saved the file.

3.  **Run the script:** Execute the script using the Python interpreter:
    ```bash
    python download_simulator.py
    ```

4.  **Follow the menu:** The script will present a menu with the following options:
    ```
    Download Simulator Menu:
    1. Set Download Speed (Bps, Kbps, Mbps, Gbps, Tbps, Pbps)
    2. Download and Select Size (MB)
    3. Exit
    ```

    * **Option 1: Set Download Speed**
        * Enter `1` and press Enter.
        * You will be prompted to enter the desired download speed along with its unit (e.g., `10 Mbps`, `1024 Kbps`, `1 Bps`, `0.5 Gbps`, etc.).
        * Enter a valid numerical value and unit, then press Enter. The script will confirm the set speed.

    * **Option 2: Download and Select Size**
        * Ensure you have set the download speed first. If not, choose option 1.
        * Enter `2` and press Enter.
        * You will be prompted to enter the file size to download in MB (megabytes).
        * Enter a positive numerical value and press Enter.
        * The script will begin simulating the download process, showing the progress in the terminal.
        * Once the simulation is complete, it will display the total download time.

    * **Option 3: Exit**
        * Enter `3` and press Enter to close the simulator.

## Requirements

* **Python 3.x:** This script is written in Python 3 and requires a Python 3 interpreter to run.

## Author

coolgaming-2011 (MrKaminK11)

## License

This program was licensed by MIT license, see [LICENSE](LICENSE) for details :)
