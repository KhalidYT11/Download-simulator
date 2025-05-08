# Python Download Simulator

This Python script simulates a file download with a user-defined download speed and file size. It provides a simple command-line interface to set the download speed (in Bps, Kbps, Mbps, Gbps, Tbps, or Pbps) and then simulate downloading a file (specifying the size in B, Kb, Mb, Gb, Tb, or Pb), showing a progress update in the terminal with slight random speed fluctuations for a more realistic simulation.

## Features

* **Set Download Speed:** Allows the user to specify the simulated download speed using various units (Bps, Kbps, Mbps, Gbps, Tbps, Pbps).
* **Select Download Size:** Enables the user to enter the size of a file to download using various units (B, Kb, Mb, Gb, Tb, Pb).
* **Simulate Download:** Simulates the download process based on the set speed and selected size, with minor random variations in speed.
* **Progress Display:** Shows a dynamic progress update in the terminal during the simulated download, indicating the amount downloaded and the percentage complete (displayed in MB for readability).
* **Estimated Time:** Displays the total time taken for the simulated download to complete.

## How to Use

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/KhalidYT11/Download-simulator/](https://github.com/KhalidYT11/Download-simulator/)
    cd Download-simulator
    ```

2.  **Run the script:** Execute the Python script using the Python interpreter:
    ```bash
    python download_simulator.py
    ```

3.  **Follow the menu:** The script will present a menu with the following options:
    ```
    Download Simulator Menu:
    1. Set Download Speed (Bps, Kbps, Mbps, Gbps, Tbps, Pbps)
    2. Select Download Size (B, Kb, Mb, Gb, Tb, Pb)
    3. Simulate Download
    4. Exit
    ```

    * **Option 1: Set Download Speed**
        * Enter `1` and press Enter.
        * You will be prompted to enter the desired download speed (e.g., `10 Mbps`, `1024 Kbps`, `1 Bps`, `0.5 Gbps`).
        * Enter a positive numerical value followed by the unit (Bps, Kbps, Mbps, Gbps, Tbps, Pbps) and press Enter. The script will confirm the set speed.

    * **Option 2: Select Download Size**
        * Enter `2` and press Enter.
        * You will be prompted to enter the file size to download (e.g., `500 Mb`, `1024 Kb`, `1 Gb`).
        * Enter a positive numerical value followed by the unit (B, Kb, Mb, Gb, Tb, Pb) and press Enter. The script will confirm the selected size.

    * **Option 3: Simulate Download**
        * Enter `3` and press Enter to start the download simulation using the previously set speed and size.

    * **Option 4: Exit**
        * Enter `4` and press Enter to close the simulator.

## Requirements

* **Python 3.x:** This script is written in Python 3 and requires a Python 3 interpreter to run.

## License

This program was licensed by the [MIT License](LICENSE), see `LICENSE` for details :)
