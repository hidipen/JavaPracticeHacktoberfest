import os

def file_info(filepath):
    if os.path.exists(filepath):
        size = os.path.getsize(filepath)
        print(f"File: {filepath}\nSize: {size} bytes")
    else:
        print("File does not exist.")

# Example usage
file_info('/path/to/file.txt')
