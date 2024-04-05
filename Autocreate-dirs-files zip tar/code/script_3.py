from pathlib import Path
import shutil
import os
import tarfile

# Display the current working directory
print(f"Current working directory: {os.getcwd()}")

# Prompt the user for the directory to be compressed
directory_to_compress = input("Enter the directory to be compressed (relative to the current working directory if not an absolute path): ")
directory_to_compress = os.path.abspath(directory_to_compress)  # Convert to absolute path
print(f"Looking for directory: {directory_to_compress}")

# Prompt the user for the location and name of the tar file
tar_file_location = input("Enter the location where you want to store the tar file (relative to the current working directory if not an absolute path): ")
tar_file_location = os.path.abspath(tar_file_location)  # Convert to absolute path
print(f"Will store the tar file in: {tar_file_location}")

# Create the directory if it doesn't exist
os.makedirs(tar_file_location, exist_ok=True)

tar_file_name = input("Enter the name of the tar file: ")

# Create the full path for the tar file
tar_file_path = Path(tar_file_location) / f'{tar_file_name}.tar.gz'

# Compress the directory using tar
with tarfile.open(tar_file_path, "w:gz") as tar:
    tar.add(directory_to_compress, arcname=os.path.basename(directory_to_compress))

print(f"Compressed the directory {directory_to_compress} into the file {tar_file_path}")
