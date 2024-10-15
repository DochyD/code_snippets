"""Renaming files."""

import os

INPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rename_files_data')
PREFIX_1 = "shot"
PREFIX_2 = "img"

def batch_rename_files(directory, prefix_1, prefix_2, start_number=1):
    """Batch rename files.
    
    Renames a file from shot_001.jpg to img_001.jpg ande vice versa
    """
    
    new_prefix = prefix_1 if os.listdir(directory)[0].startswith(prefix_2) else prefix_2
    old_prefix = prefix_2 if os.listdir(directory)[0].startswith(prefix_2) else prefix_1
    
    for count, filename in enumerate(sorted(os.listdir(directory)), start_number):
        new_name = filename.replace(old_prefix, new_prefix)
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, new_name)
        os.rename(src, dst)

batch_rename_files(INPUT_DIR, PREFIX_1, PREFIX_2)
