from pathlib import Path
import shutil
import os

# Display the current working directory
print(f"Current working directory: {os.getcwd()}")

# Prompt the user for the directory to be zipped
directory_to_zip = input("Enter the directory to be zipped (relative to the current working directory if not an absolute path): ")
directory_to_zip = os.path.abspath(directory_to_zip)  # Convert to absolute path
print(f"Looking for directory: {directory_to_zip}")

# Prompt the user for the location and name of the zip file
zip_file_location = input("Enter the location where you want to store the zip file (relative to the current working directory if not an absolute path): ")
zip_file_location = os.path.abspath(zip_file_location)  # Convert to absolute path
print(f"Will store the zip file in: {zip_file_location}")

zip_file_name = input("Enter the name of the zip file: ")

# Create the full path for the zip file
zip_file_path = Path(zip_file_location) / f'{zip_file_name}.zip'

# Zip the directory
shutil.make_archive(zip_file_path.with_suffix(''), 'zip', directory_to_zip)

print(f"Zipped the directory {directory_to_zip} into the file {zip_file_path}")
