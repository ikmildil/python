# Automating Directory and File Operations with Python

Hello everyone! Today, we’re diving into the world of Python scripts that are designed to make our lives easier by automating tasks related to directories and files. These scripts are perfect examples of Python’s power to turn tedious tasks into a breeze, saving us precious time and effort. These scripts can be incredibly useful when you need to swiftly generate sample directories and fill them with files.

Python’s readability is a standout feature, which is why I’ll be sharing the code right here in this post, as well as in a ‘code’ directory. This way, you won’t have to jump between pages; everything you need is right here.

You’ll notice that I use the terms ‘folder’ and ‘directory’ interchangeably throughout this post. When you’re juggling between different environments like Windows and Linux, it’s easy to get these terms mixed up. But don’t worry, whether I say ‘folder’ or ‘directory’, I’m talking about the same thing.

## Script 1: Creating Nested Directories and Files
The first script we’ll look at creates a nested directory structure with a specified depth and generates a certain number of files in each directory. It also creates a record file in each directory, listing the names, sizes, creation times, modification times, and types (file or directory) of all its children.
This script uses the pathlib module to handle file paths, the nltk.corpus module to generate random words for file names, and the time module to get the creation and modification times of files.
Here’s a brief overview of what the script does:

- It prompts the user for the base directory, maximum depth, and number of files. 
- It calls a recursive function that creates a new directory at each level of depth. 
- In each new directory, it creates a specified number of text files with random words as names. 
- It also creates a record file in each directory, listing the details of all its children. 
- The function calls itself to create the next level of directories and files, until the specified depth is reached. 


script_1.py

```
from pathlib import Path
import nltk
import random
import time

# Import the list of words from the nltk corpus
from nltk.corpus import words
word_list = words.words()

def create_nested_dirs(base_dir, max_depth, file_count, current_depth=1):
    """
    This function creates a nested directory structure with a specified depth and generates a certain number of files in each directory.
    It also creates a record file in each directory, listing the names, sizes, creation times, modification times, and types (file or directory) of all its children.
    """

    # Base case: if the current depth is greater than the maximum depth, stop the recursion
    if current_depth > max_depth:
        return

    # Create a new directory at the current depth
    new_dir = base_dir / f'directory_{current_depth}'
    new_dir.mkdir(parents=True, exist_ok=True)

    # Create a specified number of distinct text files in the new directory
    for i in range(1, file_count + 1):
        word = random.choice(word_list)
        (new_dir / f'{word}_{i}.txt').touch()

    # Create a record file in the new directory
    with open(new_dir / f'record_{new_dir.name}.txt', 'w') as f:
        for child in new_dir.iterdir():
            f.write(f'Name: {child.name}\n')
            f.write(f'\tType: {"Directory" if child.is_dir() else "File"}\n')
            f.write(f'\tFull Path: {child.resolve()}\n')
            f.write(f'\tSize: {child.stat().st_size} bytes\n')
            f.write(f'\tCreated: {time.ctime(child.stat().st_ctime)}\n')
            f.write(f'\tModified: {time.ctime(child.stat().st_mtime)}\n')

    # Recursively create the nested directory and files
    create_nested_dirs(new_dir, max_depth, file_count, current_depth+1)

# Prompt the user for the base directory, maximum depth, and number of files
base_dir = Path(input("Enter the base directory for creating nested directories: "))
max_depth = int(input("Enter the maximum depth of the directory structure: "))
file_count = int(input("Enter the number of files to be created in each directory: "))

# Call the function to create nested directories
create_nested_dirs(base_dir, max_depth, file_count)

```



<img src="/Autocreate-dirs-files-zip-tar/pics/python_dir_zip_tar_1.png" width="500" />



## Script 2: Zipping a Directory
The second script we’ll discuss takes a whole folder and pack it into a single zip file. We will make use of the folder/directory created in script 1.
This is really handy when you want to share a folder with someone or just keep a backup.
When you run this script, it will ask you for two things:
- The folder that you want to pack into a zip file. 
- Where you want to save the zip file and what its name should be. 

script_2.py

```
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

```



<img src="/Autocreate-dirs-files-zip-tar/pics/python_dir_zip_tar_2.png" width="500" />




## Script 3: Compressing a Directory Using Tar
The third script is similar to the second one, but it uses the tar utility for compression instead of zip. The tar utility can provide better compression ratios than zip depending on the data.
This script prompts the user for the directory to be compressed and the location and name of the tar file. It then uses the tarfile module to create a tar archive of the directory.
When you run this script, it will ask you for two things, just like the second script:
- The folder that you want to pack into a tar file. 
- Where you want to save the tar file and what its name should be. 

script_3.py

```
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

```


<img src="/Autocreate-dirs-files-zip-tar/pics/python_dir_zip_tar_3.png" width="500" />



