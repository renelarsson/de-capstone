import os
import requests

def download_day_ahead_file(url, output_path):
    """
    Downloads the day-ahead market file from the given URL and saves it to the specified output path.

    Args:
        url (str): The URL of the file to download.
        output_path (str): The local path to save the downloaded file.

    Returns:
        None
    """
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise an error for bad HTTP status codes

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Write the file to the output path
    with open(output_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

if __name__ == "__main__":
    # Example usage for quick testing
    url = "https://www.iso-ne.com/histRpts/da-lmp/WW_DALMP_ISO_20260317.csv"
    output_path = "data/raw/WW_DALMP_ISO_20260317.csv"
    download_day_ahead_file(url, output_path)