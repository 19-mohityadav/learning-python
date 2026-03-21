# Python file detection

import os

file_path = "test.txt"  # For absolute file path be careful with \

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists!")
else:
    print(f"The location '{file_path}' does not exist!")

