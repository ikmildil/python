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
