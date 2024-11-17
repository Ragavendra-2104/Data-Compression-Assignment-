import urllib.request
import gzip
import os

def calculate_compression_ratio(url):
    print("Downloading dataset...")
    response = urllib.request.urlopen(url)
    original_data = response.read()
    original_size = len(original_data)

    compressed_data = gzip.compress(original_data)
    compressed_size = len(compressed_data)

    compression_ratio = original_size / compressed_size

    original_size_mb = original_size / (1024 * 1024)
    compressed_size_mb = compressed_size / (1024 * 1024)

    print(f"Original Size: {original_size_mb:.2f} MB")
    print(f"Compressed Size: {compressed_size_mb:.2f} MB")
    print(f"Compression Ratio: {compression_ratio:.2f}")

if __name__ == "__main__":
    dataset_url = 'http://mattmahoney.net/dc/enwik9.zip'
    calculate_compression_ratio(dataset_url)
