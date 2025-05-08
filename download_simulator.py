import time
import random

def convert_to_bytes_per_second(speed_value, speed_unit):
    """Converts a speed value with its unit to bytes per second."""
    unit = speed_unit.lower()
    if unit == 'bps':
        return speed_value
    elif unit == 'kbps':
        return speed_value * 1024 / 8
    elif unit == 'mbps':
        return speed_value * 1024 * 1024 / 8
    elif unit == 'gbps':
        return speed_value * 1024 * 1024 * 1024 / 8
    elif unit == 'tbps':
        return speed_value * 1024 * 1024 * 1024 * 1024 / 8
    elif unit == 'pbps':
        return speed_value * 1024 * 1024 * 1024 * 1024 * 1024 / 8
    else:
        return None

def set_download_speed():
    """Allows the user to set the simulated download speed with unit selection."""
    while True:
        speed_str = input("Enter the desired download speed (e.g., 10 Mbps): ").strip()
        parts = speed_str.split()
        if len(parts) == 2:
            try:
                speed_value = float(parts[0])
                speed_unit = parts[1].lower()
                bytes_per_second = convert_to_bytes_per_second(speed_value, speed_unit)
                if bytes_per_second is not None and speed_value > 0:
                    return bytes_per_second
                else:
                    print("Invalid speed or unit. Please use formats like '10 Mbps', '1024 Kbps', '1 bps', etc.")
            except ValueError:
                print("Invalid speed value. Please enter a number.")
        else:
            print("Invalid input format. Please use formats like '10 Mbps'.")

def select_download_size():
    """Allows the user to select the simulated download size in MB."""
    while True:
        try:
            size_mb = float(input("Enter the file size to download in MB: "))
            if size_mb > 0:
                return size_mb
            else:
                print("Please enter a positive file size.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def simulate_download(file_size_mb, download_speed_bps):
    """Simulates a file download with a given size and speed in bytes per second, with random fluctuations."""
    if download_speed_bps <= 0:
        print("Download speed is zero or negative. Cannot simulate download.")
        return

    total_bytes = file_size_mb * 1024 * 1024
    downloaded_bytes = 0
    start_time = time.time()

    while downloaded_bytes < total_bytes:
        elapsed_time = time.time() - start_time
        # Introduce a slight random fluctuation in the download speed
        current_speed = download_speed_bps * (1 + random.uniform(-0.05, 0.05))  # +/- 5% variation
        downloaded_bytes = min(total_bytes, int(elapsed_time * current_speed))
        percentage = (downloaded_bytes / total_bytes) * 100
        downloaded_mb = downloaded_bytes / (1024 * 1024)
        print(f"Downloaded: {downloaded_mb:.2f} MB / {file_size_mb:.2f} MB ({percentage:.2f}%)", end='\r')
        time.sleep(0.1)

    end_time = time.time()
    actual_download_time = end_time - start_time
    print(f"\nDownload complete in {actual_download_time:.2f} seconds.")

def main():
    """Main function to run the download simulator."""
    download_speed_bps = 0  # Initialize download speed in bytes per second

    while True:
        print("\nDownload Simulator Menu:")
        print("1. Set Download Speed (Bps, Kbps, Mbps, Gbps, Tbps, Pbps)")
        print("2. Download and Select Size (MB)")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            download_speed_bps = set_download_speed()
            if download_speed_bps is not None:
                print("Download speed set.")
        elif choice == '2':
            if download_speed_bps > 0:
                file_size = select_download_size()
                print(f"Simulating download of {file_size:.2f} MB...")
                simulate_download(file_size, download_speed_bps)
            else:
                print("Please set the download speed first (option 1).")
        elif choice == '3':
            print("Exiting the download simulator.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
