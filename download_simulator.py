import time
import random

def set_download_speed():
    """Allows the user to set the simulated download speed."""
    while True:
        try:
            speed_mbps = float(input("Enter the desired download speed in Mbps: "))
            if speed_mbps > 0:
                return speed_mbps / 8  # Convert Mbps to MB/s
            else:
                print("Please enter a positive download speed.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def simulate_download(file_size_mb, download_speed_mps):
    """Simulates a file download with a given size and speed."""
    if download_speed_mps <= 0:
        print("Download speed is zero or negative. Cannot simulate download.")
        return

    download_time_seconds = file_size_mb / download_speed_mps
    downloaded_bytes = 0
    total_bytes = file_size_mb * 1024 * 1024  # Convert MB to bytes
    bytes_per_second = download_speed_mps * 1024 * 1024

    start_time = time.time()
    while downloaded_bytes < total_bytes:
        elapsed_time = time.time() - start_time
        downloaded_bytes = min(total_bytes, int(elapsed_time * bytes_per_second))
        percentage = (downloaded_bytes / total_bytes) * 100
        downloaded_mb = downloaded_bytes / (1024 * 1024)
        print(f"Downloaded: {downloaded_mb:.2f} MB / {file_size_mb:.2f} MB ({percentage:.2f}%)", end='\r')
        time.sleep(0.1)  # Simulate progress update frequency

    end_time = time.time()
    actual_download_time = end_time - start_time
    print(f"\nDownload complete in {actual_download_time:.2f} seconds.")

def select_download_size():
    """Allows the user to select the simulated download size."""
    while True:
        try:
            size_mb = float(input("Enter the file size to download in MB: "))
            if size_mb > 0:
                return size_mb
            else:
                print("Please enter a positive file size.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """Main function to run the download simulator."""
    download_speed = 0  # Initialize download speed

    while True:
        print("\nDownload Simulator Menu:")
        print("1. Set Download Speed")
        print("2. Download and Select Size")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            download_speed = set_download_speed()
            print(f"Download speed set to {download_speed * 8:.2f} Mbps.")
        elif choice == '2':
            if download_speed > 0:
                file_size = select_download_size()
                print(f"Simulating download of {file_size:.2f} MB at {download_speed * 8:.2f} Mbps...")
                simulate_download(file_size, download_speed)
            else:
                print("Please set the download speed first (option 1).")
        elif choice == '3':
            print("Exiting the download simulator.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
