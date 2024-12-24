# Automation logic

import os
import shutil

def copy_files():
    print("Starting the file copying process...")
    
    # Read directories from a text file
    with open('directories.txt', 'r') as file:
        lines = file.readlines()
        source_dir = lines[0].split('=')[1].strip()
        dest_dir = lines[1].split('=')[1].strip()

    # Create destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Copy files from source to destination
    for filename in os.listdir(source_dir):
        full_file_name = os.path.join(source_dir, filename)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest_dir)

    print("Files have been copied successfully.")