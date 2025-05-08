import time
import random

def convert_speed_to_bps(speed_value, speed_unit):
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

def convert_size_to_bytes(size_value, size_unit):
    """Converts a file size value with its unit to bytes."""
    unit = size_unit.lower()
    if unit == 'b':
        return size_value
    elif unit == 'kb':
        return size_value * 1024
    elif unit == 'mb':
        return size_value * 1024 * 1024
    elif unit == 'gb':
        return size_value * 1024 * 1024 * 1024
    elif unit == 'tb':
        return size_value * 1024 * 1024 * 1024 * 1024
    elif unit == 'pb':
        return size_value * 1024 * 1024 * 1024 * 1024 * 1024
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
                bytes_per_second = convert_speed_to_bps(speed_value, speed_unit)
                if bytes_per_second is not None and speed_value > 0:
                    return bytes_per_second
                else:
                    print("Invalid speed or unit. Please use formats like '10 Mbps', '1024 Kbps', '1 bps', etc.")
            except ValueError:
                print("Invalid speed value. Please enter a number.")
        else:
            print("Invalid input format. Please use formats like '10 Mbps'.")

def select_download_size():
    """Allows the user to select the simulated download size with unit selection."""
    while True:
        size_str = input("Enter the file size to download (e.g., 100 Mb): ").strip()
        parts = size_str.split()
        if len(parts) == 2:
            try:
                size_value = float(parts[0])
                size_unit = parts[1].lower()
                total_bytes = convert_size_to_bytes(size_value, size_unit)
                if total_bytes is not None and size_value > 0:
                    return total_bytes
                else:
                    print("Invalid size or unit. Please use formats like '100 Mb', '1024 Kb', '1 b', etc.")
            except ValueError:
                print("Invalid size value. Please enter a number.")
        else:
            print("Invalid input format. Please use formats like '100 Mb'.")

def simulate_download(total_bytes, download_speed_bps):
    """Simulates a file download with a given total size (in bytes) and speed in bytes per second, with random fluctuations."""
    if download_speed_bps <= 0:
        print("Download speed is zero or negative. Cannot simulate download.")
        return

    downloaded_bytes = 0
    start_time = time.time()

    while downloaded_bytes < total_bytes:
        elapsed_time = time.time() - start_time
        # Introduce a slight random fluctuation in the download speed
        current_speed = download_speed_bps * (1 + random.uniform(-0.05, 0.05))  # +/- 5% variation
        downloaded_bytes = min(total_bytes, int(elapsed_time * current_speed))
        percentage = (downloaded_bytes / total_bytes) * 100

        # Display progress in MB for better readability
        total_mb = total_bytes / (1024 * 1024)
        downloaded_mb = downloaded_bytes / (1024 * 1024)
        print(f"Downloaded: {downloaded_mb:.2f} MB / {total_mb:.2f} MB ({percentage:.2f}%)", end='\r')
        time.sleep(0.1)

    end_time = time.time()
    actual_download_time = end_time - start_time
    print(f"\nDownload complete in {actual_download_time:.2f} seconds.")

def main():
    """Main function to run the download simulator."""
    download_speed_bps = 0  # Initialize download speed in bytes per second
    total_bytes_to_download = 0 # Initialize total bytes to download

    while True:
        print("\nDownload Simulator Menu:")
        print("1. Set Download Speed (Bps, Kbps, Mbps, Gbps, Tbps, Pbps)")
        print("2. Select Download Size (B, Kb, Mb, Gb, Tb, Pb)")
        print("3. Simulate Download")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            download_speed_bps = set_download_speed()
            if download_speed_bps is not None:
                print("Download speed set.")
        elif choice == '2':
            total_bytes_to_download = select_download_size()
            if total_bytes_to_download is not None:
                print("Download size selected.")
        elif choice == '3':
            if download_speed_bps > 0 and total_bytes_to_download > 0:
                print("Simulating download...")
                simulate_download(total_bytes_to_download, download_speed_bps)
            elif download_speed_bps <= 0:
                print("Please set the download speed first (option 1).")
            elif total_bytes_to_download <= 0:
                print("Please select the download size first (option 2).")
            else:
                print("Please set both download speed and size.")
        elif choice == '4':
            print("Exiting the download simulator.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
